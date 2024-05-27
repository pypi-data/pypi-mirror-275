from functools import partial
from pathlib import Path
import typing as t


def relative_to_cwd(path_str: str):
    path = Path(path_str)
    if path.is_relative_to(Path.cwd()):
        path = path.relative_to(Path.cwd())
    return path


def update_original_wrapper(wrapper: t.Callable, f: t.Callable):
    attr = '__original_wrapped__'
    value = getattr(wrapper, attr, f)
    setattr(wrapper, attr, value)
    return wrapper


def original_wraps(wrapped: t.Callable):
    return partial(update_original_wrapper, f=wrapped)
