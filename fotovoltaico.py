from turtle import Turtle, Screen
t = Turtle()
s = Screen()
t.penup()
t.goto(-600, -300)
t.pendown()
t.speed("fastest")
# dimensioni 300x300
for i in range(0, 3):
    t.begin_fill()
    t.forward(300)
    t.backward(300)
    t.left(30)
    t.forward(300)
    t.right(30)
    t.forward(300)
    t.left(210)
    #t.right(150)
    t.forward(300)
    t.right(210)
    #t.left(150)
    t.fillcolor("silver")
    t.end_fill()
t.backward(900)
t.left(180)
print(t.heading())
for i in range(0, 4):
    t.right(150)
    t.forward(300 / 8)
    t.right(30)
    t.forward(900)
    t.left(30)
    t.forward(300 / 8)
    t.left(150)
    t.forward(900)
    print(t.heading())
t.right(180)
for i in range(0, 22):
    t.forward(20)
    t.right(150)
    t.forward(300)
    t.right(210)
    t.forward(20)
    t.left(30)
    t.forward(300)
    t.right(30)
t.forward(20)
t.penup()
t.goto(0, -50)
t.pendown()
# sun
t.color("yellow")
for i in range(0, 151):
    t.circle(radius=i)
        #if i >= 0 and i <= 100:
        #t.color("orange")
        #t.circle(radius=i)
    #elif i > 100 and i <= 151:
        #t.color("yellow")
        #t.circle(radius=i)
t.right(45)
t.forward(200)
t.backward(200)
t.left(45)
# fino a 130 degree
for i in range(0, 13):
    print("i=",i)
    t.circle(radius=150, extent=5)
    angle1 = t.heading()
    print("angle1=",angle1)
    #t.right(5+45)
    #print(t.heading())
    t.setheading(315)
    t.forward(100)
    t.backward(100)
    t.setheading(angle1)
    t.circle(radius=150, extent=5)
    angle2 = t.heading()
    print("angle2=",angle2)
    #t.right(10+45)
    # #print(t.heading())
    t.setheading(315)
    t.forward(200)
    t.backward(200)
    t.setheading(angle2)
t.right(180)
t.circle(radius=-150, extent=130)
t.left(45)
t.forward(200)
t.backward(200)
t.right(45)
for i in range(0, 13):
    print("i=",i)
    t.circle(radius=-150, extent=5)
    angle3 = t.heading()
    print("angle3=",angle3)
    #t.left(5+45)
    # #print(t.heading())
    t.setheading(225)
    t.forward(100)
    t.backward(100)
    t.setheading(angle3)
    t.circle(radius=-150, extent=5)
    angle4 = t.heading()
    print("angle4=",angle4)
    t.setheading(225)
    t.forward(200)
    t.backward(200)
    t.setheading(angle4)
t.right(180)
t.circle(radius=150, extent=130)
t.right(90)
t.forward(200)
t.backward(200)
for i in range(0, 4):
    print("i=",i)
    angle5=t.heading()
    print("angle5=",angle5)
    t.right(5)
    angle6=t.heading()
    print("angle6=",t.heading())
    t.forward(100)
    t.backward(100)
    t.right(5)
    t.forward(200)
    t.backward(200)
t.left(40)
for i in range(0, 4):
    print("i=",i)
    t.left(5)
    angle7=t.heading()
    print("angle7=",angle7)
    t.forward(100)
    t.backward(100)
    t.left(5)
    angle8=t.heading()
    print("angle8",angle8)
    t.forward(200)
    t.backward(200)
s.mainloop()
