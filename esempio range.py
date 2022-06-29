from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.speed("fastest")
t.penup()
t.goto(0,-100)
t.pendown()
for i in range(0,851):
    if i>=0 and i<=250:
        t.begin_fill()
        t.color("black")
        t.forward(i)
        t.left(120)
        t.end_fill()
        print("i black=",i)
    elif i>250 and i<=350:
        t.color("red")
        t.forward(i)
        t.left(120)
        print("i red=", i)
    elif i>350 and i<=450:
        t.color("orange")
        t.forward(i)
        t.left(120)
        print("i orange=", i)
    elif i>450 and i <=550:
        t.color("yellow")
        t.forward(i)
        t.left(120)
        print("i yellow=", i)
    elif i>550 and i <=650:
        t.color("green")
        t.forward(i)
        t.left(120)
        print("i green=", i)
    elif i>650 and i <=750:
        t.color("light blue")
        t.forward(i)
        t.left(120)
        print("i light blue=", i)
    elif i>750 and i <=850:
        t.color("purple")
        t.forward(i)
        t.left(120)
        print("i purple=", i)
       
s.mainloop()