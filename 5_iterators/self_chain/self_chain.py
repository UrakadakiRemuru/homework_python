from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for iterable in iterables:
        yield from iterable

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.obj = iterables
        self.inner_index = 0
        self.external_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            cur_elem = list(self.obj[self.external_index])
        except IndexError:
            raise StopIteration
        else:
            try:
                result = cur_elem[self.inner_index]
            except IndexError:
                self.external_index += 1
                self.inner_index = 0
                return next(self)
            else:
                self.inner_index += 1
                return result
