import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(1)

for i in range(300):
    t.forward(i/5)
    t.right(10)

t.screen.mainloop()
