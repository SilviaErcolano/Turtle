from turtle import Turtle,Screen
t=Turtle()
s=Screen()
s.bgcolor("light yellow")
t.speed(2)
t.begin_fill()
t.circle(radius=50,extent=330)
t.left(200)
t.circle(radius=100,extent=345)
t.fillcolor("yellow")
t.end_fill()
x=t.xcor()
y=t.ycor()
print("x=",x,"y=",y)
#occhio1
t.penup()
t.goto(-10,80)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(radius=5,extent=360)
t.end_fill()
#occhio2
t.penup()
t.goto(20,70)
t.pendown()
t.begin_fill()
t.circle(radius=5,extent=360)
t.end_fill()
#becco
t.penup()
t.goto(-15,30)
t.pendown()
t.begin_fill()
t.right(100)
t.circle(radius=-8,extent=160)
t.right(400)
t.circle(radius=-8,extent=160)
t.fillcolor("orange")
t.end_fill()
#zampa1
t.penup()
t.goto(-20,-190)
t.pendown()
t.color("orange")
t.end_fill()
t.right(150)
t.width(2)
t.forward(50)
t.left(45)
t.forward(20)
t.backward(20)
t.right(45)
t.forward(20)
t.backward(20)
t.right(45)
t.forward(20)
t.backward(20)
t.left(45)
#zampa2
t.penup()
t.goto(-100,-175)
t.pendown()
t.forward(50)
t.left(45)
t.forward(20)
t.backward(20)
t.right(45)
t.forward(20)
t.backward(20)
t.right(45)
t.forward(20)
t.backward(20)
s.mainloop()