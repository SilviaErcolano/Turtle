from turtle import *
t=Turtle()
s=Screen()
a=2.5
b=12
ip=(a**2+b**2)**1/2

t.color("orange")
t.begin_fill()
t.right(45/2)
t.forward(ip)
t.left(45)
t.forward(ip)
t.left(135)
t.forward(ip)
t.left(45)
t.forward(ip)
t.right(135)
t.forward(ip)
t.left(45)
t.forward(ip)
t.left(135)
t.forward(ip)
t.left(45)
t.forward(2*ip)
t.right(45)
t.forward(ip)
t.right(135)
t.forward(ip)
t.right(45)
t.forward(ip)
t.left(90)
t.forward(ip)
t.left(45)
t.forward(ip)
t.left(135)
t.forward(ip)
t.left(45)
t.forward(ip)
t.end_fill()
s.mainloop()