from turtle import Turtle,Screen
s=Turtle()
o=Screen()
from math import pi
pigreco=pi
s.width(2)
s.speed("fastest")
o.bgcolor("purple")
s.color("red")
s.width(2)
s.speed("fastest")
s.penup()
s.goto(20,-200)
s.pendown()
i=0
while i <=59:
    i=i+1
    print("iwhile=", i)
    s.left(40)
    s.circle(radius=200,extent=2*pigreco*200)
    if i in range(0,10):
        print("ired=",i)
        s.color("red")
    elif i in range(10,20):
        print("iorange=",i)
        s.color("orange")
    elif i in range(20,30):
        print("iyellow=",i)
        s.color("yellow")
    elif i in range(30,40):
        print("imagenta=",i)
        s.color("magenta")
    elif i in range(40,50):
        print("ilightblue=",i)
        s.color("lightblue")
    #elif i in range(50, 61):
    elif i in range(50,60):
        print("ilightgreen=",i)
        s.color("lightgreen")
o.mainloop()