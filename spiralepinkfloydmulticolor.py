from turtle import *
t=Turtle()
s=Screen()
a=int()
t.speed(15)
t.color("black")
for a in range(0,2400):

    if a in range(0,401):
        t.color("red")
    elif a in range(401,801):
        t.color("orange")

    elif a in range(801,1221):
        t.color("brown")
    elif a in range(1201,2400):
        t.color("black")


    t.forward(a)
    x = t.xcor()
    y = t.ycor()
    print("a=", a)
    print("x=", x)
    print("y=", y)
    t.right(135)




s.mainloop()