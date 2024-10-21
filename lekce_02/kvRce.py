a = int(input("Zadejte hodnotu koeficientu u kvadratického členu:"))
b = int(input("Zadejte hodnotu koeficientu u lineárního členu:"))
c = int(input("Zadejte hodnotu koeficientu u absolutního členu:"))

D = b**2 - 4*a*c

if a != 0:
    if D > 0:
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)
        print("x1 = ", x1, "x2 = ", x2)
    elif D == 0:
        x = (-b / (2*a))
        print("x1,2 = ", x)
    else:
        print("Chyba. Nelze řešení na R.")
else:
    print("Chyba. Není kvadratická rovnice.")
