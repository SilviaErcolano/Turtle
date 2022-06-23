from turtle import Turtle,Screen
s=Turtle()
o=Screen()
from math import pi
pigreco=pi
s.color("pink")
s.width(2)
s.speed("fastest")
o.bgcolor("light blue")
s.color("black")
s.width(2)
s.speed("fastest")
s.penup()
s.goto(20,-200)
s.pendown()
for i in range (0,60):
    print("ifor=", i)
    s.left(40)
    s.circle(radius=200,extent=2*pigreco*200)
    if i in range(0,10):
        print("iblack=",i)
        s.color("black")
    elif i in range(10,20):
        print("ibrown=",i)
        s.color("brown")
    elif i in range(20,30):
        print("igrey=",i)
        s.color("grey")
    elif i in range(30,40):
        print("igreen=",i)
        s.color("green")
    elif i in range(40,50):
        print("iblue=",i)
        s.color("blue")
    elif i in range(50,60):
        print("ired=",i)
        s.color("red")

o.mainloop()
