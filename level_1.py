from caesar import encode_text
from ui import red, green


def level_1():
  while True:
    try:
      shift = int(input("Bitte geben Sie die Verschiebung ein: "))
      break
    except ValueError:
      print(red('Falsche Eingabe! Bitte geben Sie eine Zahl ein.'))
  text = input("Bitte geben Sie den Text ein: ")
  print(green(f'\nVerschlüsselter Text: '))
  print(encode_text(text, shift))
