from collections.abc import Generator
from contextlib import contextmanager
from types import FunctionType, ModuleType
from typing import TypeVar

T = TypeVar("T")


def add_enter_exit_methods(cls: T) -> T:
    if hasattr(cls, "Dispose") and not hasattr(cls, "__enter__"):
        # Define the __enter__ method
        def __enter__(self: T) -> Generator[T]:
            return self

        # Assign the __enter__ method to the class
        cls.__enter__ = FunctionType(__enter__.__code__, globals(), "__enter__")

    if hasattr(cls, "Dispose") and not hasattr(cls, "__exit__"):
        # Define the __exit__ method
        def __exit__(self: T, exc_type, exc_value, traceback) -> None:
            self.Dispose()

        # Assign the __exit__ method to the class
        cls.__exit__ = FunctionType(__exit__.__code__, globals(), "__exit__")

    return cls


def enable_with_for_module(module: ModuleType):
    import inspect

    members = inspect.getmembers(module)
    import System

    disposable_classes = [
        obj
        for _, obj in members
        if inspect.isclass(obj) and issubclass(obj, System.IDisposable)
    ]

    for cls in disposable_classes:
        add_enter_exit_methods(cls)


@contextmanager
def using(obj: T) -> Generator[T]:
    try:
        yield obj
    finally:
        if hasattr(obj, "Dispose"):
            obj.Dispose()
        elif hasattr(obj, "Close"):
            obj.Close()
