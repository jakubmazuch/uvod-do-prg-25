def deleni(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except OverflowError:
        return None
    except ValueError:
        return None
    except TypeError:
        return None


delitel = float(input("Zadejte dělitele: "))
delenec = float(input("Zadejte dělence: "))
deleni(delenec, delitel)
