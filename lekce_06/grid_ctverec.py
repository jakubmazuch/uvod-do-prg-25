import turtle


def ctverec(velikost):
    for i in range(4):
        turtle.forward(velikost)
        turtle.right(90)


def grid(velikost, pocet):
    for y in range(pocet):
        for x in range(pocet):
            ctverec(velikost)
            turtle.forward(velikost)
        turtle.backward(velikost * pocet)
        turtle.right(90)
        turtle.forward(velikost)
        turtle.left(90)


# nastavení želvy
turtle.shape("turtle")
turtle.speed(100)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid(10, 5)

turtle.done()
