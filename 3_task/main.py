"""
Напиши программу, которая принимает на вход телефон и стандартизирует его, печатая в стандартизированном виде.

Формат телефона, который должен быть на выходе: 8 (9xx) xxx-xx-xx, например, 8 (901) 123-45-67.

Форматы телефонов на входе:

89xxxxxxxxx, например, 89011234567
9xxxxxxxxx — пропущена первая 7 или 8, например, 9011234567
79xxxxxxxxx, например, 79011234567
+79xxxxxxxxx, например, +79011234567
форматы выше с любыми нечисловыми символами в строке, например:
8 __()-! 901-123-45-67,
+7901-123-45   67,
#@!(zz8901-___123-45gg67 какая-то ещё петрушка R$&*z
и тп. Все нечисловые символы должны быть проигнорированы при анализе телефонного номера, после очистки номер должен совпасть по формату с одним из шаблонов, перечисленных в 1-4 пунктах.
Если телефон не подходит по формату ничему перечисленному, программа выводит на печать исходный телефон, в котором оставлены только цифры.
"""


def format_phone(phone_number: str) -> dict[str, int]:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    formatted_phone_number = ""

    return formatted_phone_number
