from turtle import *
t=Turtle()
s=Screen()
a=2.5
b=12
ip=(a**2+b**2)**1/2
#for i in range(0,16):

t.color("red")
t.begin_fill()
t.left(45)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.backward(ip)
t.left(135)
t.end_fill()
t.forward(20)
t.color("green")
t.begin_fill()
t.left(45)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.left(45)
t.end_fill()
t.forward(10)
t.color("yellow")
t.begin_fill()
t.right(90)
t.forward(10)
t.left(45)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.left(45)
t.end_fill()
t.forward(10)

t.color("blue")
t.begin_fill()
t.forward(10)
t.left(45)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.right(90)
t.forward(ip)
t.end_fill()



s.mainloop()