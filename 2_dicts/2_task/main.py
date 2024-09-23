import re

def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    pattern = r'[.,:;!?—()«»\'"…`  \n]'
    most_common = {}
    words_list = [elem.lower() for elem in re.split(pattern, text) if len(elem) >= 3]

    for word in words_list:
        if word in most_common:
            most_common[word] += 1
        else:
            most_common[word] = 1

    l = sorted(list(most_common.items()), key=lambda x: (-x[1], x[0]), reverse=True)[:-11:-1]
    most_common = dict(l)

    return most_common
