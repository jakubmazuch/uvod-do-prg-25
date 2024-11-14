def eratoshtenovo_sito(n):
    n += 1
    sito = [True] * n
    for i in range(2, n):
        if sito[i]:
            for j in range(2*i, n, i):
                sito[j] = False
    prvocisla = []
    for i in range(2, n):
        if sito[i]:
            prvocisla.append(i)
    return prvocisla


vstup = int(input("Zadej číslo: "))
print(eratoshtenovo_sito(vstup))
