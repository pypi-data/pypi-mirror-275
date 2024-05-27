from contextlib import ContextDecorator
from time import perf_counter


class timeit(ContextDecorator):
    def __init__(self, print_tmpl: str = "it takes {:.5f} s"):
        """Measure the time of a block of code.

        Args:
            print_tmpl (str, optional): Print template. Defaults to "it takes {:.5f} s".

        Examples:
            >>> # doctest: +SKIP
            >>> with timeit():
            ...     # do something here
            ...     pass
        """
        self._print_tmpl: str = print_tmpl
        self._start_time: float

    def __enter__(self):
        self._start_time = perf_counter()

    def __exit__(self, exec_type, exec_value, traceback):
        print(self._print_tmpl.format(perf_counter() - self._start_time))


__all__ = ["timeit"]
