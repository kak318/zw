import os

if os.name == "posix":
  clear = "clear"
else:
  clear = "cls"

numm = int(input("Wybież numer od 1 do 9\n> "))

print("Obliczam...")
numm = numm * 2
numm = numm + 5
numm = numm * 50

urodziny = input("Miałeś w tym roku urodziny? [tak/nie]\n> ")
if urodziny == "tak" or urodziny == "nie":
  if urodziny == "tak":
    numm = numm + 1768
  elif urodziny == "nie":
    numm = numm + 1767
else:
  print("Wybież 'tak' lub 'nie'")

year = int(input("Twój rok urodzenia\n> "))
print("Obliczam...")

numm = numm - year
numm = numm + 3

os.system(clear)
print(numm)
print("Pierwsza liczba to numer który wybrałeś na początku\nA dwie inne to twój wiek")
print("*Notatka: Działa tylko w 2021")
input()
