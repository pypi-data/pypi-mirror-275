from collections import defaultdict
from typing import Callable, DefaultDict, TypeVar

from fastcore.dispatch import TypeDispatch

T = TypeVar("T")

DSIPATCH_REGISTRY: DefaultDict[str, TypeDispatch] = defaultdict(TypeDispatch)


def typedispatch(is_impl: bool = True) -> Callable[[T], T]:
    def _inner(f: T) -> T:
        if isinstance(f, (classmethod, staticmethod)):
            name = f"{f.__func__.__qualname__}"
        elif hasattr(f, "__qualname__"):
            name = f"{f.__qualname__}"
        else:
            raise TypeError(f"Unsupported type: {type(f)}")

        if isinstance(f, classmethod):
            f = f.__func__  # type: ignore
        if is_impl:
            DSIPATCH_REGISTRY[name].add(f)
        return DSIPATCH_REGISTRY[name]  # type: ignore

    return _inner


__all__ = ["typedispatch"]
