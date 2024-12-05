def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seznam = [0, 1]
    for _ in range(2, n):
        seznam.append(seznam[-1] + seznam[-2])
    return seznam


n = int(input("Zadejte číslo: "))
if n < 1:
    print("Zadejte kladné číslo.")
else:
    print("Prvních", n, "členů Fibonacciho posloupnosti je:", fibonacci(n))
