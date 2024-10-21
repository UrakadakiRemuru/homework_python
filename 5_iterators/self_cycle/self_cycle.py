from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    copy_of_iterable = []
    for elem in obj:
        copy_of_iterable.append(elem)
        yield elem

    while True:
        yield from copy_of_iterable

class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = list(obj)
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.obj[self.ind]
        except IndexError:
            self.ind = 0
            return next(self)
        else:
            self.ind += 1
            return result
