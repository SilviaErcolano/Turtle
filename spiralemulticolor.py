from turtle import Turtle,Screen
i=Turtle()
h=Screen()
i.turtlesize(0.5)
i.speed(15)
a=int()
for a in range(0,1364):

    if a in range(0,101):
        i.color("black")
    elif a in range(101,202):
         i.color("grey")
    elif a in range(202,303):
        i.color("brown")
    elif a in range(303,404):
        i.color("red")
    elif a in range(404,505):
        i.color("purple")
    elif a in range(505,606):
        i.color("orange")
    elif a in range(606,707):
        i.color("green")
    elif a in range(707,808):
        i.color("yellow")
    elif a in range(808,909):
        i.color("pink")
    elif a in range(909,1010):
     i.color("light blue")
    elif a in range(1010,1111):
        i.color("black")
    elif a in range(1111,1212):
        i.color("grey")
    elif a in range(1212,1313):
        i.color("brown")
    elif a in range(1313,1364):
      i.color("red")

    i.forward(a)
    i.right(90)
    print("a=",a)
    x=i.xcor()
    y=i.ycor()
    print("x=",x)
    print("y=",y)





h.mainloop()
