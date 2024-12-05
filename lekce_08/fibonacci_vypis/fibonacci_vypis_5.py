def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end="|")
        a, b = b, a + b
    print()


n = int(input("Zadejte přirozené číslo: "))
fibonacci(n)
