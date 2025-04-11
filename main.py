from level_1 import level_1
from level_2 import level_2
from level_3 import level_3
from ui import red


# todo: Stufen beschreiben
LEVELS = {
  "auf der Kommandozeile eingegebenen Text verschlüsseln": level_1,
  "Text aus \"klartext.txt\" verschlüsseln und in \"geheimtext.txt\" speichern": level_2,
  "(Beschreibung 3)": level_3,
}

if __name__ == "__main__":
  flag = True
  while flag:
    print("Hallo! Bitte geben Sie den Nummer der Stufe ein. Geben Sie 0 ein, um das Programm zu beenden")

    descriptions = list(LEVELS.keys())

    for i in range(len(LEVELS)):
      print(f'{i+1}. Stufe: {descriptions[i]}')

    while True:
      try:
        id = int(input('Ihre Eingabe: '))

        if (id == 0):
          break

        if (id not in range(1, len(LEVELS) + 1)):
          print(red('Falsche Eingabe! Solcher Nummer existiert nicht'))
          continue

        break
      except ValueError:
        print(red('Falsche Eingabe! Bitte geben Sie eine Zahl ein.'))

    LEVELS[descriptions[int(id) - 1]]()

    while True:
      print("")
      print("Wollen Sie das Programm noch einmal benutzen? (y/n)")
      answer = input()
      if answer == 'y':
        print("")
        break
      elif answer == 'n':
        flag = False
        break
      else:
        print(red("Falsche Eingabe! Bitte geben Sie entweder y oder n ein."))
