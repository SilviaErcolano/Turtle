from turtle import *
t=Turtle()
s=Screen()
t.pencolor("grey")
#cerchio1
t.begin_fill()
t.fillcolor("pink")
t.penup()
t.goto(100,0)
t.pendown()
#t.forward(100)
a=15
i=(a**2+a**2)**(1/2)
t.left(45)
t.forward(i)
t.backward(i)
t.left(135)
t.penup()
t.goto(0,0)
t.pendown()
t.right(135)
t.forward(i)
t.left(45)
t.circle(radius=-50)
t.left(135)
t.forward(i)
t.left(45)
t.circle(radius=50)
t.end_fill()
#freccia
t.begin_fill()
t.circle(radius=50,extent=90)
t.right(90)
t.forward(120)
t.left(135)
t.forward(i)
t.left(45)
t.forward(120)
t.left(135)
t.forward(i)
t.end_fill()
t.begin_fill()
t.backward(i)
t.left(45)
t.forward(70)
t.left(135)
t.forward(i)
t.backward(i)
t.left(45)
t.forward(15)
t.right(45)
t.forward(i)
t.right(135)
t.forward(15)
t.right(90)
t.left(45)
t.forward(i)
t.right(135)
t.forward(15)
t.end_fill()
t.left(135)
t.forward(i)
t.left(45)
t.forward(15)
t.left(135)
t.forward(i)
t.backward(i)
t.begin_fill()
t.right(180)
t.forward(i)
t.backward(i)
t.right(135)
t.forward(15)
t.left(135)
t.forward(i)
t.left(45)
t.forward(15)
t.end_fill()
t.hideturtle()
s.exitonclick()
s.mainloop()