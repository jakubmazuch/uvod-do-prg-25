def vstup():
    x = int(input("Zadejte číslo: "))
    print(x+1)


while True:
    try:
        vstup()
        break
    except ValueError as e:
        print("Špatný vstup. ", e, " Zkuste to znovu.")
