def hledameNejmladsiOsobu(cesta):
    nejmladsiOsoba = None
    minimalniVek = float('inf')

    with open(cesta, 'r', encoding='utf-8') as soubor:
        for radek in soubor:
            jmenaPrijmeni, vek = radek.strip().split(',')
            vek = int(vek)

            if vek < minimalniVek:
                minimalniVek = vek
                nejmladsiOsoba = jmenaPrijmeni

    return minimalniVek, nejmladsiOsoba


cesta = 'lekce_09\jmenaVek.csv'
print(hledameNejmladsiOsobu(cesta))
