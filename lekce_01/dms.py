# stupne minuty vteriny do dekadickeho zapisu
d = int(input("Zadej stupne: "))
m = int(input("Zadej minuty: "))
s = int(input("Zadej vteriny: "))
x = d + m/60 + s/3600
print("Úhel: ", x)

# dekadicky do st, min, vt
stupne = float(input("Zadejte dekadicky zapis:"))
d2 = int(stupne)
m2 = int((stupne - d2) * 60)
s2 = int(((stupne - d2) * 60 - m2) * 60)
print(d2, "° ", m2, "' ", s2, "''")