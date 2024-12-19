import math


class Koule:
    def __init__(self, polomer):
        self.polomer = polomer

    def vypocet_objemu(self):
        return 4/3 * math.pi * self.polomer ** 3

    def vypocet_povrchu(self):
        return 4 * math.pi * self.polomer ** 2

    def __str__(self):
        return f"Koule o poloměru {self.polomer} m"


if __name__ == "__main__":
    try:
        polomer = float(input("Zadejte poloměr koule v metrech: "))
        if polomer <= 0:
            raise ValueError("Poloměr musí být kladné číslo")
        else:
            koule = Koule(polomer)
            print(koule)
            print(f"Objem koule je {koule.vypocet_objemu()} m³")
            print(f"Povrch koule je {koule.vypocet_povrchu()} m²")
    except ValueError:
        print("Zadaná hodnota není číslo.")
