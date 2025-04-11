from string import ascii_lowercase

# lowercase alphabet
ALPHABET = ascii_lowercase


def encode_symbol(symbol: str, shift: int) -> str:
  if symbol.lower() in ALPHABET:
    index = ALPHABET.index(symbol.lower())
    shifted_index = (index + shift) % len(ALPHABET)
    raw_symbol = ALPHABET[shifted_index]
    return raw_symbol.lower() if raw_symbol == raw_symbol.lower() else raw_symbol.upper()
  return symbol


def encode_text(text: str, shift: int) -> str:
  return "".join([encode_symbol(s, shift) for s in text])


text = "abcde"
shift = 1

print(encode_text(text, shift))
