from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.speed("fastest")
t.penup()
t.goto(0,-20)
t.pendown()
t.forward(40)
t.right(90)
t.forward(300)
t.right(90)
t.forward(40)
t.right(90)
t.forward(300)
a = 40
i = (a ** 2 + a ** 2) ** (1 / 2)
print(i)
t.right(45)
t.forward(i)
t.right(45)
t.forward(40)
t.right(135)
t.forward(i)
t.left(45)
t.forward(300)
t.left(135)
t.forward(i)
t.left(45)
t.forward(300)
t.left(90)
t.left(45)
t.forward(i)
t.right(45)
t.forward(20)
# cerchiogrande1
t.width(3)
t.begin_fill()
t.circle(radius=-140)
t.fillcolor("magenta")
#t.fillcolor("light yellow")
t.end_fill()
t.right(180)
t.forward(20)
t.left(45)
t.width(0)
t.pencolor("magenta")
#t.pencolor("light yellow")
t.forward(i)
t.left(135)
t.forward(20)
t.width(3)
t.circle(radius=-100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(radius=50)
t.circle(radius=50,extent=180)
t.right(90)
t.forward(50)
#colorazione
t.begin_fill()
t.fillcolor("purple")
#t.fillcolor("brown")
#t.pencolor("brown")
t.pencolor("purple")
t.right(90)
t.circle(radius=-100,extent=180)
t.right(90)
t.forward(50)
t.right(90)
t.circle(radius=50,extent=180)
t.right(90)
t.forward(50)
t.end_fill()
t.begin_fill()
t.left(90)
t.circle(radius=100,extent=180)
t.left(90)
t.forward(50)
t.left(90)
t.circle(radius=-50,extent=180)
t.left(90)
t.forward(50)
t.end_fill()
t.backward(50)
t.begin_fill()
t.fillcolor("black")
#t.fillcolor("grey")
t.right(90)
t.circle(radius=-50)
t.end_fill()
t.penup()
#centro quadrato- incentro
t.goto(20,-40)
t.pendown()
t.width(0)
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-80)
t.pendown()
t.pencolor("grey")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-120)
t.pendown()
t.pencolor("magenta")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-160)
t.pendown()
t.pencolor("purple")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-200)
t.pendown()
t.pencolor("grey")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-240)
t.pendown()
t.pencolor("magenta")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(20,-280)
t.pendown()
t.pencolor("purple")
for i in range(0,40):
    t.forward(i)
    t.right(90)
t.penup()
t.goto(0,-320)
t.pendown()
t.pencolor("grey")
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(20)
t.left(90)
t.forward(40)
t.left(90)
t.forward(20)
t.fillcolor("grey")
t.end_fill()
t.left(90)
t.forward(40)
t.begin_fill()
t.left(45)
a = 40
i = (a ** 2 + a ** 2) ** (1 / 2)
t.forward(i)
t.left(45)
t.forward(20)
t.left(135)
t.forward(i)
t.left(45)
t.forward(20)
t.end_fill()
t.pencolor("magenta")
t.penup()
t.goto(t.xcor(),t.ycor()+20)
t.pendown()
t.begin_fill()
t.fillcolor("magenta")
t.right(180)
t.forward(280)
t.right(45)
t.forward(i)
t.right(135)
t.forward(280)
t.right(45)
t.forward(i)
t.end_fill()
t.penup()
t.goto(0,-20)
t.pendown()
t.pencolor("black")
t.right(225)
t.penup()
t.goto(20,-20)
t.pendown()
t.width(3)
t.circle(radius=140)
t.penup()
t.goto(40,-60)
t.pendown()
t.begin_fill()
#t.fillcolor("grey")
t.pencolor("black")
t.fillcolor("black")
t.left(45)
t.forward(i)
t.right(135)
t.forward(i)
t.right(45)
t.forward(i)
t.right(135)
t.forward(i)
t.end_fill()
t.right(45)
t.forward(i/2)
t.right(135)
t.forward(i)
t.backward(i/2)
t.left(135)
#t.end_fill()
t.pencolor("magenta")
t.width(0)
for i in range(0,20):
    t.circle(radius=-i,extent=180)
t.penup()
t.goto(40,-60)
t.pendown()
t.end_fill()
t.right(135)
ip=56.568542494923804
t.color("black")
t.forward(ip)
t.begin_fill()
t.color("purple")
t.forward(ip)
t.left(135)
t.forward(ip)
t.left(45)
t.forward(ip)
t.left(135)
t.forward(ip)
t.end_fill()
t.backward(ip/2)
t.left(45)
t.forward(ip/2)
t.right(45)
t.right(180)
t.color("black")
t.right(45)
for i in range(0,38):
    t.forward(i)
    t.left(120)
t.penup()
t.goto(40,-60)
t.pendown()
t.setheading(0)
t.right(90)
t.forward(ip)
t.color("purple")
t.forward(ip)
t.begin_fill()
t.color("grey")
t.forward(ip)
t.left(135)
t.forward(ip)
t.left(45)
t.forward(ip)
t.left(135)
t.forward(ip)
t.end_fill()
t.left(45)
t.forward(ip/2)
t.left(135)
t.forward(ip/2)
t.color("purple")
t.right(45)
for i in range(0,45):
    t.forward(i)
    t.right(135)
t.hideturtle()
s.mainloop()
