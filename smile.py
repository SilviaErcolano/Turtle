from turtle import *
t=Turtle()
s=Screen()
#t.width(2)
t.begin_fill()
t.circle(radius=100,extent=360)
t.fillcolor("yellow")
t.end_fill()
x=t.xcor()
y=t.ycor()
print("x=",x,"y=",y)
t.penup()
t.goto(-30,150)
t.pendown()
t.begin_fill()
t.circle(radius=5,extent=360)
t.fillcolor("black")
t.end_fill()
t.penup()
t.goto(-25,140)
t.pendown()
t.circle(radius=15,extent=360)
t.penup()
t.goto(30,150)
t.pendown()
t.begin_fill()
t.circle(radius=5,extent=360)
t.end_fill()
t.penup()
t.goto(35,140)
t.pendown()
t.circle(radius=15,extent=360)
t.penup()
t.goto(-70,50)
t.pendown()
t.right(60)
t.circle(radius=70,extent=120)


s.mainloop()