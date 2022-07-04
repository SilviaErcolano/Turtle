import turtle
t=turtle.Turtle()
d=turtle.Screen()
t.turtlesize(0.5)
d.bgcolor("brown")
""""
d.colormode(255)
R=153
G=102
B=51
d.bgcolor((R,G,B))
"""
a=int()
t.width(2)
t.speed(15)
t.color("white")
for a in range(0,601):
    t.left(45)
    t.forward(a)
    t.right(90)
    print("a=",a)
    x=t.xcor()
    y=t.ycor()
    print("x=",x)
    print("y=",y)
d.mainloop()
