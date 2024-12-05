while True:
    try:
        x = float(input("Zadejte dělence: "))
        y = float(input("Zadejte dělitele: "))
        print(x/y)
    except ValueError:
        print("None")
    except ZeroDivisionError:
        print("None")
    except OverflowError:
        print("None")
    else:
        break
