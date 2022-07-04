from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.speed("fastest")
t.penup()
t.goto(0,-100)
t.pendown()
i=0
while i<=850:
    i=i+1
    if i>=1 and i<=251:
        t.begin_fill()
        t.color("black")
        t.forward(i)
        t.left(120)
        t.end_fill()
        print("i black=",i)
    elif i>251 and i<=351:
        t.color("red")
        t.forward(i)
        t.left(120)
        print("i red=", i)
    elif i>351 and i<=451:
        t.color("orange")
        t.forward(i)
        t.left(120)
        print("i orange=", i)
    elif i>451 and i <=551:
        t.color("yellow")
        t.forward(i)
        t.left(120)
        print("i yellow=", i)
    elif i>551 and i <=651:
        t.color("green")
        t.forward(i)
        t.left(120)
        print("i green=", i)
    elif i>651 and i <=751:
        t.color("light blue")
        t.forward(i)
        t.left(120)
        print("i light blue=", i)
    elif i>751 and i <=851:
        t.color("purple")
        t.forward(i)
        t.left(120)
        print("i purple=", i)
s.mainloop()
