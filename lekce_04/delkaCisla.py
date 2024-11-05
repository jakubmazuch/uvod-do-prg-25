a = int(input("Zadej číslo: "))
a = abs(a)

if a < 10:
    print("Číslo je jednociferné.")
elif a < 100:
    print("Číslo je dvouciferné.")
elif a < 1000:
    print("Číslo je trojciferné.")
elif a < 10000:
    print("Číslo je čtyřciferné.")
else:
    print("Číslo je víceciferné.")
