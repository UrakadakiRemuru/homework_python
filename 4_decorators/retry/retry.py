# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])
import time
from typing import Callable
from datetime import timedelta


def retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exception)] = (Exception,)) -> Callable:
    if count < 1:
        raise ValueError

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except handled_exceptions:
                    if attempt + 1 == count:
                        raise
                time.sleep(delay.total_seconds())
        return wrapper

    return decorator
