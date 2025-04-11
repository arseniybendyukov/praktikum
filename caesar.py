from string import ascii_uppercase


# uppercase alphabet
ALPHABET = ascii_uppercase


def encode_symbol(symbol: str, shift: int) -> str:
  if symbol.upper() in ALPHABET:
    index = ALPHABET.index(symbol.upper())
    shifted_index = (index + shift) % len(ALPHABET)
    raw_symbol = ALPHABET[shifted_index]
    return raw_symbol.lower() if symbol == symbol.lower() else raw_symbol.upper()
  return symbol


def encode_text(text: str, shift: int) -> str:
  return "".join([encode_symbol(s, shift) for s in text])
