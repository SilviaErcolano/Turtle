from turtle import *
t=Turtle()
s=Screen()
t.left(45)
t.penup()
t.goto(0,-200)
t.pendown()
b=2
b1=4
b2=8
b3=16
b4=32
b5=64
b6=128
b7=256
b8=512

if b==2 or b1==4 or b2==8 or b3==16 or b4==32 or b5==64 or b6==128 or b7==256 or b8==512:
    t.begin_fill()
    a=(b**2+b**2)**(1/2)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(135)
    t.forward(3*b)
    t.right(135)
    t.fillcolor("black")
    t.end_fill()
    t.begin_fill()
    a1 = (b1 ** 2 + b1 ** 2) ** (1 / 2)
    t.forward(a1)
    t.right(90)
    t.forward(a1)
    t.right(135)
    t.forward(3 * b1)
    t.right(135)
    t.fillcolor("purple")
    t.begin_fill()
    t.begin_fill()
    a2 = (b2 ** 2 + b2 ** 2) ** (1 / 2)
    t.forward(a2)
    t.right(90)
    t.forward(a2)
    t.right(135)
    t.forward(3 * b2)
    t.right(135)
    t.fillcolor("green")
    t.end_fill()
    t.begin_fill()
    a3 = (b3 ** 2 + b3 ** 2) ** (1 / 2)
    t.forward(a3)
    t.right(90)
    t.forward(a3)
    t.right(135)
    t.forward(3 * b3)
    t.right(135)
    t.fillcolor("pink")
    t.end_fill()
    t.begin_fill()
    a4 = (b4 ** 2 + b4 ** 2) ** (1 / 2)
    t.forward(a4)
    t.right(90)
    t.forward(a4)
    t.right(135)
    t.forward(3 * b4)
    t.right(135)
    t.fillcolor("yellow")
    t.end_fill()
    t.begin_fill()
    a5 = (b5 ** 2 + b5 ** 2) ** (1 / 2)
    t.forward(a5)
    t.right(90)
    t.forward(a5)
    t.right(135)
    t.forward(3 * b5)
    t.right(135)
    t.fillcolor("orange")
    t.end_fill()
    t.begin_fill()
    a6 = (b6 ** 2 + b6 ** 2) ** (1 / 2)
    t.forward(a6)
    t.right(90)
    t.forward(a6)
    t.right(135)
    t.forward(3 * b6)
    t.right(135)
    t.fillcolor("red")
    t.end_fill()
    t.begin_fill()
    a7 = (b7 ** 2 + b7 ** 2) ** (1 / 2)
    t.forward(a7)
    t.right(90)
    t.forward(a7)
    t.right(135)
    t.forward(3 * b7)
    t.right(135)
    t.fillcolor("black")
    t.end_fill()
    t.begin_fill()
    a8 = (b8 ** 2 + b8 ** 2) ** (1 / 2)
    t.forward(a8)
    t.right(90)
    t.forward(a8)
    t.right(135)
    t.forward(2 * b8)
    t.right(135)
    t.fillcolor("purple")
    t.end_fill()
    t.begin_fill()


s.mainloop()