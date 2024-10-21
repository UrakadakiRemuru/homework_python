from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    if n < 1:
        raise ValueError('n must be at least one')
    start = 0
    end = n
    while True:
        try:
            result = tuple(obj[start:end])
        except IndexError:
            if start > len(obj):
                break
            elif end > len(obj):
                yield tuple(obj[start:])
        else:
            start = end
            end += n
            yield result


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        if n < 1:
            raise ValueError('n must be at least one')
        self.obj = list(obj)
        self.start = 0
        self.stop = n
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = tuple(self.obj[self.start:self.stop])
        except IndexError:
            if self.start > len(self.obj):
                raise StopIteration
            elif self.stop > len(self.obj):
                return tuple(self.obj[self.start:])
        else:
            self.start = self.stop
            self.stop += self.n
            return result
