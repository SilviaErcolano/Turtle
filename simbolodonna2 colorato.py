from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.pencolor("black")
t.width(10)
#1
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(200)
t.right(90)
t.forward(30)
t.right(90)
t.forward(200)
t.fillcolor("pink")
t.end_fill()
#2
t.begin_fill()
a=30
i=(a**2+a**2)**(1/2)
print(i)
t.right(45)
t.forward(i)
t.right(45)
t.forward(30)
t.right(135)
t.forward(i)
t.end_fill()
#3
t.begin_fill()
t.left(45)
t.forward(200)
t.left(135)
t.forward(i)
t.left(45)
t.forward(200)
t.left(135)
t.forward(i)
t.end_fill()
#4
t.backward(i)
t.right(45)
t.forward(15)
t.begin_fill()
t.circle(radius=-70)
t.end_fill()
#5
t.backward(15)
t.left(45)
t.forward(i)
t.right(45)
t.forward(15)
t.begin_fill()
t.circle(radius=-70)
t.end_fill()
#6
print(t.xcor(),t.ycor())
t.penup()
t.goto(15.000000000000064 ,1.4876988529977098e-13+20)
t.pendown()
t.begin_fill()
t.circle(radius=-50)
t.fillcolor("white")
t.end_fill()
#7
t.penup()
t.goto(15.000000000000064 ,1.4876988529977098e-13+140)
t.pendown()
t.begin_fill()
t.right(135)
t.forward(i)
#t.fillcolor("grey")
#t.end_fill()
#8
t.right(45)
t.circle(radius=-70,extent=90)
t.right(45)
t.forward(i)
t.left(45)
t.circle(radius=-70,extent=90)
t.backward(15)
t.left(90)
t.forward(120)
t.begin_fill()
t.right(90)
t.forward(90)
t.left(90)
t.forward(30)
t.left(90)
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(150)
t.fillcolor("pink")
t.end_fill()
t.begin_fill()
t.right(135)
t.forward(i)
t.right(45)
t.forward(150)
t.right(135)
t.forward(i)
t.end_fill()
t.begin_fill()
t.left(45)
t.forward(30)
t.left(135)
t.forward(i)
t.left(45)
t.forward(30)
t.left(135)
t.forward(i)
t.end_fill()
t.hideturtle()
s.exitonclick()
#s.mainloop()