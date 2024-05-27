from functools import partial
from functools import wraps
from itertools import cycle
from itertools import repeat
from itertools import tee
import logging
import time
import typing as t

from .utils import original_wraps
from .utils import relative_to_cwd


# try:
#     from typing import ParamSpec
# except ImportError:
#     from typing_extensions import ParamSpec  # type: ignore[assignment]
# P = ParamSpec('P')  # https://docs.python.org/zh-tw/3/library/typing.html#typing.ParamSpec
# R = t.TypeVar('R')
FuncT = t.Callable  # [P, R]


logger = logging.getLogger(__package__)


_T = t.TypeVar('_T')
SingleOrTuple = t.Union[_T, tuple[_T, ...]]
SingleOrIterable = t.Union[_T, t.Iterable[_T]]


SleepT = t.Callable[[float], None]
DelayT = float
RetriesT = t.Optional[int]
LogfT = t.Callable[[t.Any], None]


class DummyLogger(logging.Logger):
    def __init__(self, logf: LogfT):
        self._logf = logf
        super().__init__(__package__ or __name__)

    def _log(self, level, msg, *args, **kwargs):
        self._logf(msg)


def sleep_on_start(
    seconds: DelayT,
    *,
    sleep: SleepT = time.sleep,
    logger: logging.Logger = logger,
):
    if not isinstance(logger, logging.Logger):
        logger = DummyLogger(logger)

    def decorator(f):
        @original_wraps(f)
        @wraps(f)
        def wrapper(*args, **kwds):
            wf = wrapper.__original_wrapped__
            finfo = f'{relative_to_cwd(wf.__code__.co_filename)}:{wf.__code__.co_firstlineno}'
            logger.info(f'{wf.__qualname__} sleep {seconds} seconds on start ({finfo})')
            sleep(seconds)
            return f(*args, **kwds)

        return wrapper

    return decorator


def _fork_delays(delays: SingleOrIterable[DelayT]):
    if not isinstance(delays, t.Iterable):
        delays = repeat(delays)
    delays, delays_ = tee(delays)
    delays_ = cycle(delays_)
    return delays, delays_


def retry(
    retries: RetriesT = None,
    *,
    exceptions: SingleOrTuple[t.Type[Exception]] = Exception,
    error_callback: t.Optional[t.Callable[[int, Exception, DelayT, RetriesT, FuncT], None]] = None,
    sleep: SleepT = time.sleep,
    delays: SingleOrIterable[DelayT] = 0,
    first_delay: t.Optional[DelayT] = None,
    chain_exception: bool = False,
    logger: t.Union[logging.Logger, LogfT] = logger,
):
    if not isinstance(logger, logging.Logger):
        logger = DummyLogger(logger)

    def _default_error_callback(i: int, e: Exception, d: DelayT, r: RetriesT, wf: FuncT):
        finfo = f'{relative_to_cwd(wf.__code__.co_filename)}:{wf.__code__.co_firstlineno}'
        is_last = i == r
        if not is_last:
            logger.info(f'{wf.__qualname__} tried {i} of {r}: {e!r} -> sleep {d} seconds ({finfo})')
        else:
            logger.warning(f'{wf.__qualname__} tried {i} of {r} -> {e!r} ({finfo})')

    error_callback = error_callback or _default_error_callback

    def callback(i: int, e: Exception, d: DelayT, r: RetriesT, wf: FuncT):
        error_callback(i, e, d, r, wf)
        if i != r:
            sleep(d)

    def decorator(f):
        @original_wraps(f)
        @wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal delays
            delays, delays_ = _fork_delays(delays)
            function_retrying = partial(f, *args, **kwargs)
            try:
                result = function_retrying()
            except exceptions as e:
                wf = wrapper.__original_wrapped__
                i = 0
                callback(i, e, first_delay or next(delays_), retries, wf)
                while True:
                    try:
                        result = function_retrying()
                    except exceptions as e:
                        i += 1
                        callback(i, e, next(delays_), retries, wf)
                        if i == retries:
                            if chain_exception:
                                raise
                            raise e from None
                    else:
                        return result
            else:
                return result

        return wrapper

    return decorator
