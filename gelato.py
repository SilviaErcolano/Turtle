from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.color("black")
#parte 1
t.begin_fill()
t.width(5)
t.left(90)
t.forward(140)
t.circle(radius=60,extent=180)
t.forward(140)
t.left(90)
t.forward(120)
t.fillcolor("pink")
t.end_fill()
t.begin_fill()
#spessore
t.backward(120)
print(t.xcor(),t.ycor())
t.left(90)
t.forward(140)
t.circle(radius=-60,extent=100)
t.left(180)
t.circle(radius=80,extent=85.74)
print(t.xcor(),t.ycor())
t.left(104.26)
print(t.heading())
t.right(90)
t.forward(120)
t.left(45)
print(t.xcor(),t.ycor())
a=-141.00799820057554+120.00000000000006
b=20.0096410985456-5.684341886080802e-14
i=(a**2+b**2)**(1/2)
t.forward(i)

t.end_fill()
#faccia
t.penup()
t.goto(-100,100)
t.pendown()
t.left(135)
t.circle(radius=-10,extent=180)
t.penup()
t.goto(-40,100)
t.pendown()
t.left(180)
t.circle(radius=-10,extent=180)
t.pendown()
t.penup()
t.goto(-80,90)
t.pendown()
t.forward(70)
t.penup()
t.goto(-20,90)
t.pendown()
t.forward(70)
#stecca
t.penup()
t.goto(-70,0)
t.pendown()
t.begin_fill()
t.forward(40)
t.circle(radius=10,extent=180)
t.forward(40)
print(t.xcor(),t.ycor())
t.left(90)
t.forward(20)
t.fillcolor("brown")
t.end_fill()


s.mainloop()