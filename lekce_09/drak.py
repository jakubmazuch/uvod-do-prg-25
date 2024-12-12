class Drak:
    def __init__(self, pocet_hlav, hmotnost, umi_letat=False, jmeno=""):
        self.pocet_hlav = pocet_hlav
        self.hmotnost = hmotnost
        self.umi_letat = umi_letat
        self.jmeno = jmeno

    def __str__(self):
        return (f"Drak {self.jmeno}: "
                f"{self.pocet_hlav} hlav, {self.hmotnost} kg, "
                f"umí létat: {'ano' if self.umi_letat else 'ne'}")


# Tvorba draků
drak1 = Drak(3, 600, True, "Bohuslav")
drak2 = Drak(9, 400, False, "Milan")

# Výpis vlastností
print(drak1)
print(drak2)

# Provnání počtu hlav
if drak1.pocet_hlav > drak2.pocet_hlav:
    print("první drak má více hlav.")
else:
    print("první drak má méně hlav.")

# Výpočet vítěze souboje
sila_drak1 = 100 * drak1.pocet_hlav + drak1.hmotnost
sila_drak2 = 100 * drak2.pocet_hlav + drak2.hmotnost

if sila_drak1 > sila_drak2:
    print("První drak vyhrál.")
elif sila_drak1 < sila_drak2:
    print("Druhý drak vyhrál.")
else:
    print("Remíza.")