from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.penup()
t.goto(-550, 330)
t.pendown()
t.fillcolor("orange")
t.speed("fastest")
x = int()
# 1
for x in range(0, 7):
    t.begin_fill()
    t.width(5)
    t.right(135)
    a = 20
    i = (a ** 2 + a ** 2) ** (1 / 2)
    print(i)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    b = 15
    c = (b ** 2 + b ** 2) ** (1 / 2)
    print(c)
    t.forward(c)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.backward(c)
    t.left(135)
    t.forward(30)
    t.right(90)
    # t.fillcolor("yellow")
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.backward(30)
    t.left(90)
    t.begin_fill()
    # t.fillcolor("magenta")
    t.forward(b)
    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(45)
    t.forward(b)
    t.right(135)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.forward(c)
    t.end_fill()
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.left(135)
    print("x0=", t.xcor(), "y0=", t.ycor())
    t.penup()
    t.goto(t.xcor() + 180, t.ycor())
    t.pendown()
    print("x=", x)
    print("x0+1=", t.xcor(), "yo+1=", t.ycor())
    if x == 0 or x == 2 or x == 4 or x == 6:
        t.fillcolor("yellow")
    if x == 1 or x == 3 or x == 5:
        t.fillcolor("orange")
# 2
t.penup()
t.goto(-550, 180)
t.pendown()
t.fillcolor("purple")
for x in range(0, 7):
    t.begin_fill()
    t.width(5)
    t.right(135)
    a = 20
    i = (a ** 2 + a ** 2) ** (1 / 2)
    print(i)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    b = 15
    c = (b ** 2 + b ** 2) ** (1 / 2)
    print(c)
    t.forward(c)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.backward(c)
    t.left(135)
    t.forward(30)
    t.right(90)
    # t.fillcolor("yellow")
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.backward(30)
    t.left(90)
    t.begin_fill()
    # t.fillcolor("magenta")
    t.forward(b)
    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(45)
    t.forward(b)
    t.right(135)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.forward(c)
    t.end_fill()
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.left(135)
    print("x0=", t.xcor(), "y0=", t.ycor())
    t.penup()
    t.goto(t.xcor() + 180, t.ycor())
    t.pendown()
    print("x=", x)
    print("x0+1=", t.xcor(), "yo+1=", t.ycor())
    if x == 0 or x == 2 or x == 4 or x == 6:
        t.fillcolor("brown")
    if x == 1 or x == 3 or x == 5:
        t.fillcolor("purple")
# 3
t.penup()
t.goto(-550, 30)
t.pendown()
t.fillcolor("green")
for x in range(0, 7):
    t.begin_fill()
    t.width(5)
    t.right(135)
    a = 20
    i = (a ** 2 + a ** 2) ** (1 / 2)
    print(i)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    b = 15
    c = (b ** 2 + b ** 2) ** (1 / 2)
    print(c)
    t.forward(c)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.backward(c)
    t.left(135)
    t.forward(30)
    t.right(90)
    # t.fillcolor("yellow")
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.backward(30)
    t.left(90)
    t.begin_fill()
    # t.fillcolor("magenta")
    t.forward(b)
    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(45)
    t.forward(b)
    t.right(135)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.forward(c)
    t.end_fill()
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.left(135)
    print("x0=", t.xcor(), "y0=", t.ycor())
    t.penup()
    t.goto(t.xcor() + 180, t.ycor())
    t.pendown()
    print("x=", x)
    print("x0+1=", t.xcor(), "yo+1=", t.ycor())
    if x == 0 or x == 2 or x == 4 or x == 6:
        t.fillcolor("light green")
    if x == 1 or x == 3 or x == 5:
        t.fillcolor("green")
# 4
t.penup()
t.goto(-550, -120)
t.pendown()
t.fillcolor("red")
for x in range(0, 7):
    t.begin_fill()
    t.width(5)
    t.right(135)
    a = 20
    i = (a ** 2 + a ** 2) ** (1 / 2)
    print(i)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    b = 15
    c = (b ** 2 + b ** 2) ** (1 / 2)
    print(c)
    t.forward(c)
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.backward(c)
    t.left(135)
    t.forward(30)
    t.right(90)
    # t.fillcolor("yellow")
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.backward(30)
    t.left(90)
    t.begin_fill()
    # t.fillcolor("magenta")
    t.forward(b)
    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(45)
    t.forward(b)
    t.right(135)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.forward(c)
    t.end_fill()
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(c)
    t.left(135)
    print("x0=", t.xcor(), "y0=", t.ycor())
    t.penup()
    t.goto(t.xcor() + 180, t.ycor())
    t.pendown()
    print("x=", x)
    print("x0+1=", t.xcor(), "yo+1=", t.ycor())
    if x == 0 or x == 2 or x == 4 or x == 6:
        t.fillcolor("blue")
    if x == 1 or x == 3 or x == 5:
        t.fillcolor("red")

s.mainloop()
# s.exitonclick()
