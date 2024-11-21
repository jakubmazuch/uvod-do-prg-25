import turtle


def trojuhelnik(strana):
    for _ in range(3):
        turtle.forward(strana)
        turtle.right(120)


def grid_trojuhelnik(strana, pocet_v_radku):
    for y in range(1, pocet_v_radku):
        for x in range(y):
            trojuhelnik(strana)
            turtle.forward(strana)
        turtle.backward(strana * y)
        turtle.right(60)
        turtle.forward(strana)
        turtle.left(60)


# nastavení želvy
turtle.shape("turtle")
turtle.speed(2)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid_trojuhelnik(50, 5)

turtle.done()
