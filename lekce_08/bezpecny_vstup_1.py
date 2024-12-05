def vstup():
    while True:
        try:
            vstup = int(input("Zadejte číslo: "))
            return vstup
        except ValueError:
            print("Špatný vstup. Zkuste to znovu.")


cislo = vstup()
print("Zadané číslo je ", cislo + 1)
