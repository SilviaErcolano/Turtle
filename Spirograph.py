from turtle import Turtle,Screen
s=Turtle()
o=Screen()
#o.bgcolor("black")
from math import pi
p=pi
s.color("pink")
s.width(2)
s.speed("fastest")
s.penup()
s.goto(0,-100)
s.pendown()
for i in range(0,60):
    print("i=",i)
    s.left(43)
    #s.circle(radius=100,extent=360)
    s.circle(radius=100,extent=2*p*100)
    if i in range(0,10):
        s.color("pink")
    elif i in range(10,20):
        s.color("orange")
    elif i in range(20,30):
        s.color("red")
    elif i in range(30,40):
         s.color("green")
    elif i in range(40,50):
        s.color("purple")
    elif i in range(50,60):
        s.color("brown")
o.mainloop()