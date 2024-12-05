def fibbonacihoCislo(x):
    try:
        a = 0
        b = 1
        for i in range(x):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
    except TypeError as e:
        raise e


n = int(input("Zadejte přirozené číslo: "))
v = fibbonacihoCislo(n)
print(v, end=" ")
