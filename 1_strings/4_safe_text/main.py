import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    list_of_raws = wrong_article.split('\n')
    sentence = ''
    pattern = 'woof-woof'
    sign = '!'
    for raw in list_of_raws:
        exclamation_mark_counter = 1
        result_list = []
        if not len(raw): continue
        for word in raw.split():
            exclamation_mark_pointer = word.find(sign)
            if exclamation_mark_pointer != -1:
                exclamation_mark_counter += len(word[:exclamation_mark_pointer])
            else:
                exclamation_mark_counter += len(word) + 1

            word = word.swapcase()[::-1]
            pointer = word.find(pattern)

            if pointer != -1:
                word = word[:pointer] + 'cat' + word[pointer + len(pattern):]

            result_list.insert(0, word)
        result_list[0] = result_list[0][exclamation_mark_counter:].capitalize()
        result_raw = ' '.join(result_list) + '.\n'
        sentence += result_raw

    return sentence

print(get_correct_article())
print(recover_article())
assert get_correct_article() == recover_article()