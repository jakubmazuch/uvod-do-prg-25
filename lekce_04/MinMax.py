a = int(input("Zadej první hodnotu: "))
b = int(input("Zadej druhou hodnotu: "))
c = int(input("Zadej třetí hodnotu: "))

# hledáme max
if a > b and a > c:
    print(f"Největší číslo je {a}.")
elif b > a and b > c:
    print(f"Největší číslo je {b}.")
else:
    print(f"Největší číslo je {c}.")

# hledáme min
if a < b and a < c:
    print(f"Nejmenší číslo je {a}.")
elif b < a and b < c:
    print(f"Nejmenší číslo je {b}.")
else:
    print(f"Nejmenší číslo je {c}.")
