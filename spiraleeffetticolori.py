from turtle import *

t = Turtle()
s = Screen()
a = int()
t.color("blue")
t.speed("fastest")
s.bgcolor("light yellow")
i = 0
while i <= 481:
    i = i + 1
    t.begin_fill()
    t.left(45)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(135)
    t.forward(i)
    t.right(135)
    t.forward(i)
    t.fillcolor("red")
    t.end_fill()
    print("i=", i)
    x = t.xcor()
    y = t.ycor()
    print("x=", x, "y=", y)

s.mainloop()
