import os.path
from datetime import datetime, UTC


class DelegateTXT:
    def __init__(self, path: str, buffer_limit: int):
        self.path = path
        self.buffer_limit = buffer_limit
        self.buffer = []
        self.buffer_counter = 0

    def create_file(self):
        with open(self.path, 'a'):
            pass

    def check_buffer(self):
        if self.buffer_counter == self.buffer_limit:
            self.buffer_counter = 0
            self.write_to_file()
            self.buffer = []

    def append_buffer(self, message: str, value: int):
        self.buffer_counter += 1
        self.buffer.append(
            (datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%S%z'), message, str(value))
        )

    def write_to_file(self, sep: str = ' '):
        string_to_write = ''
        for tup in self.buffer:
            string_to_write += sep.join(tup) + '\n'

        with open(self.path, 'a') as f:
            f.write(string_to_write)

    def incr(self, message: str):
        self.append_buffer(message, 1)
        self.check_buffer()

    def decr(self, message: str):
        self.append_buffer(message, -1)
        self.check_buffer()

    def evacuate(self):
        self.buffer_counter = 0
        self.write_to_file()
        self.buffer = []


class DelegateCSV(DelegateTXT):

    def create_file(self):
        mode = 'a'
        line = 'date;metric;value\n'
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                if not file.readlines():
                    mode = 'w'
                else:
                    line = ''
        with open(self.path, mode) as f:
            f.write(line)

    def write_to_file(self, sep=';'):
        super().write_to_file(sep)


class Statsd:
    def __init__(self, delegate: DelegateTXT):
        """Реализуйте класс"""
        self.delegate = delegate
        self.delegate.create_file()

    def __getattr__(self, item):
        if item in ['incr', 'decr']:
            return getattr(self.delegate, item)
        raise AttributeError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delegate.evacuate()


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    if path[-3:] != 'txt':
        raise ValueError
    delegate = DelegateTXT(path, buffer_limit)
    return Statsd(delegate)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    if path[-3:] != 'csv':
        raise ValueError
    delegate = DelegateCSV(path, buffer_limit)
    return Statsd(delegate)
