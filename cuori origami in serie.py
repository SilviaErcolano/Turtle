from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.penup()
t.goto(-650,300)
t.pendown()
t.speed("fastest")
s.bgcolor("yellow")
#lato 1
for i in range(0,7):
    t.width(4)
    t.pencolor("grey")
    t.begin_fill()
    t.forward(40)
    t.right(45) #A
    a=20
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
    print("x3=",t.xcor(),"y3=",t.ycor())
    #lato 4
    t.forward(40)
    t.right(90) #F'
    print("x4=",t.xcor(),"y4=",t.ycor())
    #t.circle(radius=-30,extent=180)
    #lato 5
    t.forward(60)
    print("x5=", t.xcor(), "y5=", t.ycor())
    t.right(45) #D
    b=60
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
     #lato 8
    t.forward(60)
    t.fillcolor("magenta")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    print("icuore1=",i)
    t.penup()
    t.goto(x+200,y)
    t.pendown()
    print("xspost=",t.xcor(),"yspost=",t.ycor())
    t.right(90) #orientamento dx 90 gradi
t.penup()
t.goto(-650,150)
t.pendown()
for i in range(0,7):
    t.width(4)
    t.pencolor("grey")
    t.begin_fill()
    t.forward(40)
    t.right(45) #A
    a=20
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
    print("x3=",t.xcor(),"y3=",t.ycor())
    #lato 4
    t.forward(40)
    t.right(90) #F'
    print("x4=",t.xcor(),"y4=",t.ycor())
    #t.circle(radius=-30,extent=180)
    #lato 5
    t.forward(60)
    print("x5=", t.xcor(), "y5=", t.ycor())
    t.right(45) #D
    b=60
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
     #lato 8
    t.forward(60)
    t.fillcolor("magenta")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    print("icuore2=",i)
    t.penup()
    t.goto(x+200,y)
    t.pendown()
    print("xspost=",t.xcor(),"yspost=",t.ycor())
    t.right(90) #orientamento dx 90 gradi
t.penup()
t.goto(-650,0)
t.pendown()
for i in range(0,7):
    t.width(4)
    t.pencolor("grey")
    t.begin_fill()
    t.forward(40)
    t.right(45) #A
    a=20
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
    print("x3=",t.xcor(),"y3=",t.ycor())
    #lato 4
    t.forward(40)
    t.right(90) #F'
    print("x4=",t.xcor(),"y4=",t.ycor())
    #t.circle(radius=-30,extent=180)
    #lato 5
    t.forward(60)
    print("x5=", t.xcor(), "y5=", t.ycor())
    t.right(45) #D
    b=60
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
     #lato 8
    t.forward(60)
    t.fillcolor("magenta")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    print("icuore3=",i)
    t.penup()
    t.goto(x+200,y)
    t.pendown()
    print("xspost=",t.xcor(),"yspost=",t.ycor())
    t.right(90) #orientamento dx 90 gradi
t.penup()
t.goto(-650,-150)
t.pendown()
for i in range(0,7):
    t.width(4)
    t.pencolor("grey")
    t.begin_fill()
    t.forward(40)
    t.right(45) #A
    a=20
    ip1=(a**2+a**2)**(1/2)
    #lato 2
    t.forward(ip1)
    t.left(90) #B
    #lato 3
    t.forward(ip1)
    t.right(45) #C
    print("x3=",t.xcor(),"y3=",t.ycor())
    #lato 4
    t.forward(40)
    t.right(90) #F'
    print("x4=",t.xcor(),"y4=",t.ycor())
    #t.circle(radius=-30,extent=180)
    #lato 5
    t.forward(60)
    print("x5=", t.xcor(), "y5=", t.ycor())
    t.right(45) #D
    b=60
    #lato 6
    ip2=(b**2+b**2)**(1/2)
    t.forward(ip2)
    t.right(90) #E
    #lato 7
    t.forward(ip2)
    t.right(45) #F
     #lato 8
    t.forward(60)
    t.fillcolor("magenta")
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    print("x=",x,"y=",y)
    print("icuore4=",i)
    t.penup()
    t.goto(x+200,y)
    t.pendown()
    print("xspost=",t.xcor(),"yspost=",t.ycor())
    t.right(90) #orientamento dx 90 gradi

s.mainloop()