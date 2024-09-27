import re


def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """

    pattern = r'[0-9]'
    formatted_phone_number = ''.join(re.findall(pattern, phone_number))
    number_length = len(formatted_phone_number)
    if number_length == 11:
        if formatted_phone_number[0] == '8':
            return f'{formatted_phone_number[0]} ({formatted_phone_number[1:4]}) {formatted_phone_number[4:7]}-{formatted_phone_number[7:9]}-{formatted_phone_number[9:]}'
        elif formatted_phone_number[0] == '7':
            return f'8 ({formatted_phone_number[1:4]}) {formatted_phone_number[4:7]}-{formatted_phone_number[7:9]}-{formatted_phone_number[9:]}'
    elif number_length == 10:
        return f'8 ({formatted_phone_number[0:3]}) {formatted_phone_number[3:6]}-{formatted_phone_number[6:8]}-{formatted_phone_number[8:]}'
    else:
        return formatted_phone_number
