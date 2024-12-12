import csv
from datetime import datetime

# vstup a výstup
vstup = 'lekce_09\jmena.csv'
vystup = 'lekce_09\jmenaVek.csv'


def vypocet_veku(datum_narozeni):
    dnes = datetime.now()
    narozeni = datetime.strptime(datum_narozeni, '%d.%m.%Y')
    vek = dnes.year - narozeni.year
    return vek


# Čtení a zpracování dat
vystupniData = []
with open(vstup, mode='r', encoding='utf-8') as soubor:
    ctecka = csv.reader(soubor, delimiter=';')
    for radek in ctecka:
        jmeno, datum_narozeni = radek
        vek = vypocet_veku(datum_narozeni)
        vystupniData.append([jmeno, vek])


# Tvorba výstupu
with open(vystup, mode='w', newline='', encoding='utf-8') as soubor:
    zapisovatel = csv.writer(soubor)
    for radek in vystupniData:
        zapisovatel.writerow(radek)
