import turtle


def ctverec(velikost):
    for i in range(4):
        turtle.forward(velikost)
        turtle.right(90)


# nastavení želvy
turtle.shape("turtle")
turtle.speed(1)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

ctverec(25)

turtle.done()
