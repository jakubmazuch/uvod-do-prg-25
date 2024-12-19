class AnalyzatorTeplot:
    def __init__(self):
        self.teploty = []

    def pridat_teplotu(self, teplota):
        self.teploty.append(teplota)

    def shrnuti(self):
        if not self.teploty:
            return None
        pocet = len(self.teploty)
        prumer = sum(self.teploty) / pocet
        nejvyssi = max(self.teploty)
        nejnizsi = min(self.teploty)

        return {
            "pocet": pocet,
            "prumerK": prumer,
            "prumerC": prumer - 273.15,
            "nejvyssiK": nejvyssi,
            "nejvyssiC": nejvyssi - 273.15,
            "nejnizsiK": nejnizsi,
            "nejnizsiC": nejnizsi - 273.15,
        }


def main():
    print("Zadejte hodnoty měřených teplot v Kelvinech. Pro ukončení stiskněte tlačítko 0.")

    analyzator = AnalyzatorTeplot()

    while True:
        try:
            teplota = float(input("Zadejte teplotu v K: "))
            if teplota == 0:
                break
            elif teplota < 0:
                print("Teplota nemůže být záporná")
                continue
            analyzator.pridat_teplotu(teplota)
        except ValueError:
            print("Chybný vstup")

    vyhodnoceni = analyzator.shrnuti()
    if vyhodnoceni is None:
        print("Nebyly zadná žádná platná teplota")
    else:
        print(f"Počet měření: {vyhodnoceni['pocet']}")
        print(
            f"Průměrná teplota: {vyhodnoceni['prumerK']} K ({vyhodnoceni['prumerC']} °C)")
        print(
            f"Nejvyšší teplota: {vyhodnoceni['nejvyssiK']} K ({vyhodnoceni['nejvyssiC']} °C)")
        print(
            f"Nejnižší teplota: {vyhodnoceni['nejnizsiK']} K ({vyhodnoceni['nejnizsiC']} °C)")


if __name__ == "__main__":
    main()
