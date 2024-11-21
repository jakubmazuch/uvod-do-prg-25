import turtle


def obdelnik(sirka, vyska):
    for i in range(2):
        turtle.forward(sirka)
        turtle.right(90)
        turtle.forward(vyska)
        turtle.right(90)


def grid(sirka, vyska, pocet_sirka, pocet_vyska):
    for y in range(pocet_vyska):
        for x in range(pocet_sirka):
            obdelnik(sirka, vyska)
            turtle.forward(sirka)
        turtle.backward(sirka * pocet_sirka)
        turtle.right(90)
        turtle.forward(vyska)
        turtle.left(90)


# nastavení želvy
turtle.shape("turtle")
turtle.speed(2)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid(50, 20, 6, 8)

turtle.done()
