import turtle
turtle.bgcolor("#ffe7bc")
t = turtle.Turtle()
t.speed(0)
t.color("green")

for i in range(1,100):
    for j in range(1,6):
        t.left(144)
        t.forward(200)
    t.left(5)

t.done()