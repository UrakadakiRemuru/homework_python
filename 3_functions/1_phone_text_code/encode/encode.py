from utils import KEYBOARD_SWAP

def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    text = text.lower()

    result = ""

    for symbol in text:
        try:
            encoded_symbol = KEYBOARD_SWAP[symbol]
        except KeyError:
            return

        result += encoded_symbol + ' '

    return result.rstrip()
