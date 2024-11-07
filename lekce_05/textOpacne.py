text = input("Zadej text: ")
seznam = list(text)
opacne = []

for i in range(len(seznam) - 1, -1, -1):
    opacne.append(seznam[i])

vysledek = "".join(opacne)
print("Opačný text:", vysledek)
