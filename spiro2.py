from turtle import Turtle,Screen
s=Turtle()
o=Screen()
o.bgcolor("black")
from math import pi
p=pi
s.color("black")
s.width(2)
s.speed(5)
s.penup()
s.goto(0,-100)
s.pendown()
s.color("pink")
for i in range(0,61):
 s.left(43)
 s.circle(radius=100,extent=360)
 if i in range(0,11):
     s.color("pink")
 elif i in range(11,21):
     s.color("brown")
 elif i in range(21,31):
     s.color("yellow")
 elif i in range(31,41):
     s.color("orange")
 elif i in range(51,61):
     s.color("purple")


o.mainloop()