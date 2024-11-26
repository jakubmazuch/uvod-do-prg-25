def faktorial(n):
    if n > 1:
        return n * faktorial(n-1)
    else:
        return 1


vstup = int(input("Zadejte číslo: "))
print(faktorial(vstup))
