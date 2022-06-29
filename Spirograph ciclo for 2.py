from turtle import Turtle,Screen
s=Turtle()
o=Screen()
from math import pi
pigreco=pi
s.color("pink")
s.width(2)
s.speed("fastest")
s.color("pink")
s.width(2)
s.speed("fastest")
s.penup()
s.goto(40,-200)
s.pendown()
for i in range (0,60):
    print("ifor=", i)
    s.left(40)
    s.circle(radius=200,extent=2*pigreco*200)
    if i in range(0,10):
        print("ipink=",i)
        s.color("pink")
    elif i in range(10,20):
        print("iorange=",i)
        s.color("orange")
    elif i in range(20,30):
        print("ired=",i)
        s.color("red")
    elif i in range(30,40):
        print("igreen=",i)
        s.color("green")
    elif i in range(40,50):
        print("ipurple=",i)
        s.color("purple")
    elif i in range(50,60):
        print("ibrown=",i)
        s.color("brown")
o.mainloop()

