# bankomat
b5000 = 5000
b2000 = 2000
b1000 = 1000
b500 = 500
b200 = 200
b100 = 100
b50 = 50
b20 = 20
b10 = 10
b5 = 5
b2 = 2
b1 = 1

# uživatel zadává kolik peněz si chce vybrat
m = int(input("Kolik korun si chcete vybrat? "))

n5000 = m//b5000
m = m - b5000*n5000
n2000 = m//b2000
m = m - b2000*n2000
n1000 = m//b1000
m = m - b1000*n1000
n500 = m//b500
m = m - b500*n500
n200 = m//b200
m = m - b200*n200
n100 = m//b100
m = m - b100*n100
n50 = m//b50
m = m - b50*n50
n20 = m//b20
m = m - b20*n20
n10 = m//b10
m = m - b10*n10
n5 = m//b5
m = m - b5*n5
n2 = m//b2
m = m - b2*n2
n1 = m//b1
m = m - b1*n1

print("5000: ", n5000)
print("2000: ", n2000)
print("1000: ", n1000)
print("500: ", n500)
print("200: ", n200)
print("100: ", n100)
print("50: ", n50)
print("20: ", n20)
print("10: ", n10)
print("5: ", n5)
print("2: ", n2)
print("1: ", n1)
