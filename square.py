from turtle import *
t = Turtle()
t.screen.setup(800, 800)

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(140)
t.pendown()

t.penup()
t.goto(0, 100)
t.pendown()
t.right(90)
t.forward(140)

t.screen.mainloop()
