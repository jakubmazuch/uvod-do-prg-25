def fibonacci(n):
    if n <= 0:
        print("Zadejte kladné číslo.")
        return
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print(fib[n-1])


x = int(input("Zadejte přirozené číslo: "))
fibonacci(x)
