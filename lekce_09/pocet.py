b = 0
cesta = 'lekce_09/jmena.csv'
with open(cesta, mode='r', encoding='utf-8') as a:
    for line in a:
        b += 1

print(b)
