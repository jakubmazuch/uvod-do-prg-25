def prumernyVek(cesta):
    soucetVeku = 0
    pocet = 0

    with open(cesta, 'r', encoding='utf-8') as soubor:
        for radek in soubor:
            # rozdělím si řádky na jména a věk
            casti = radek.strip().split(',')
            soucetVeku += int(casti[1].strip())
            pocet += 1

    return soucetVeku / pocet


cesta = 'lekce_09\jmenaVek.csv'
print(prumernyVek(cesta))
