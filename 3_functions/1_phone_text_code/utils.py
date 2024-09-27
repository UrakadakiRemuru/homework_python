import re

SYMBOL_DICT = {
        '1': re.split(r' ', '. , ? ! : ;'),
        '2': re.split(r' ', 'а б в г'),
        '3': re.split(r' ', 'д е ж з'),
        '4': re.split(r' ', 'и й к л'),
        '5': re.split(r' ', 'м н о п'),
        '6': re.split(r' ', 'р с т у'),
        '7': re.split(r' ', 'ф х ц ч'),
        '8': re.split(r' ', 'ш щ ъ ы'),
        '9': re.split(r' ', 'ь э ю я'),
        '0': ' '
    }


def make_keyboard(symbol_dict: dict) -> dict:
    keyboard = dict()
    for k, v in symbol_dict.items():
        if k == '0':
            keyboard.update({k: v})
        else:
            for i, symb in enumerate(v):
                keyboard.update({k * (i + 1): symb})
    return keyboard


def key_value_swap(d: dict) -> dict:
    return {v: k for k, v in d.items()}


KEYBOARD = make_keyboard(SYMBOL_DICT)
KEYBOARD_SWAP = key_value_swap(KEYBOARD)