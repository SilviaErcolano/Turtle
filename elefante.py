from turtle import *
t=Turtle()
s=Screen()
t.width(5)
t.color("light blue")
t.left(90)
t.circle(radius=100,extent=180)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.circle(radius=-50,extent=180)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.penup()
t.goto(-49.99,86.60254)
t.pendown()
t.right(90)
t.circle(radius=50,extent=180)
t.penup()
t.goto(-49.99,86.60254)
t.pendown()
t.penup()
t.goto(-150,86.60254)
t.pendown()
t.circle(radius=-50,extent=180)
t.forward(10)
t.circle(radius=50,extent=100)
t.right(90)
t.forward(20)
t.right(60)
t.circle(radius=-50,extent=70)
t.left(100)
t.forward(20)
t.penup()
t.goto(-100,40)
t.pendown()
t.color("black")
t.circle(30,60)
t.circle(-30,60)
t.hideturtle()
s.mainloop()
