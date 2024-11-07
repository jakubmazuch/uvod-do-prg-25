import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

for i in range(4):
    t.forward(100)
    t.right(90)

t.screen.mainloop()
