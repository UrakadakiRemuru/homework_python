import os

from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    api_list_of_strings = get_employees_info()
    parsed_employees_info = []
    keys_list = ['id', 'name', 'last_name', 'age', 'position', 'salary']

    for string in api_list_of_strings:
        string = string.split()
        current_key = ''
        current_dict = {}
        for i, word in enumerate(string):
            if i % 2 == 0:
                if word in keys_list:
                    current_key = word
                else:
                    current_key = ''
            else:
                if current_key in ['age', 'id']:
                    current_dict[current_key] = int(word)
                elif current_key == 'salary':
                    print(current_key, word)
                    current_dict[current_key] = Decimal(word)
                elif current_key in ['name', 'last_name', 'position']:
                    current_dict[current_key] = word
        parsed_employees_info.append(current_dict)

    return parsed_employees_info
