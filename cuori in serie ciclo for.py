from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.penup()
t.goto(-650,300)
t.pendown()
t.speed("fastest")
#lato 1
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
#Sposto in basso
t.penup()
t.goto(-650,200)
t.pendown()
#Serie 2
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
#Sposto in basso
t.penup()
t.goto(-650,100)
t.pendown()
#Serie 3
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
    #Serie 4
t.penup()
t.goto(-650,0)
t.pendown()
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
    #Serie 5
t.penup()
t.goto(-650,-100)
t.pendown()
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
#Serie 6
t.penup()
t.goto(-650,-200)
t.pendown()
for i in range(0,13):
    t.width(2)
    t.begin_fill()
    t.forward(20)
    t.right(45) #A
    a=10
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
     #lato 4
    t.forward(20)
    t.right(90) #F'
     #lato 5
    t.forward(30)
    t.right(45) #D
    b=30
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
    #lato 8
    t.forward(30)
    t.fillcolor("red")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.right(90) #orientamento dx 90
t.hideturtle()
s.mainloop()