import turtle
t = turtle.Pen()
colors = ["orange", "brown"]
turtle.bgcolor("lightblue")
for x in range(450):
    t.pencolor(colors[x%2])
    t.forward(x)
    t.left(91)