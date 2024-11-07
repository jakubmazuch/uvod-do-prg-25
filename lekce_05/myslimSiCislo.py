import random

# Definice mezí
a = int(input("Zadej dolní mez: "))
b = int(input("Zadej horní mez: "))

w = 0
if b < a:
    w = a
    a = b
    b = w

# Generování náhodného čísla
nahodne = random.randint(a, b)
skore = 0
x = int(input("Hádej číslo: "))
while x != nahodne:
    if x < nahodne:
        print("Moje číslo je větší.")
    else:
        print("Moje číslo je menší.")
    skore += 1
    x = int(input("Hádej číslo: "))

print("Gratuluji, uhádl jsi číslo", nahodne, "po", skore, "pokus(ech).")
