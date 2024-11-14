def faktorial(cislo):
    fakt = 1
    while cislo > 0:
        fakt *= cislo
        cislo -= 1
    return fakt


a = int(input("Zadej číslo: "))
print(faktorial(a))
