import re
from utils import KEYBOARD

def decode_numbers(numbers: str) -> str | None:

    numbers = numbers.lower()

    result = ""

    for number_combination in numbers.split():
        try:
            decoded_symbol = KEYBOARD[number_combination]
        except KeyError:
            return

        result += decoded_symbol
    return result