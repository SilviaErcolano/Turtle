from turtle import Turtle,Screen
i=Turtle()
h=Screen()
i.turtlesize(0.5)
i.speed(15)
#a=100
a=int()
for a in range(0,1364):
        i.forward(a)
        i.right(90)
        if a>=0 and a<=101 or a>202 and a<=303 or a>404 and a<=505 or a>606 and a<=707 or a>808 and a<=909 or a>1010 and a<=1111 or a>1212 and a<=1313:
                i.color("black")
        elif a>101 and a<=202 or a>303 and a<=404 or a>505 and a<=606 or a>707 and a<=808 or a>909 and a<=1010 or a>1111 and a<=1212 or a>1313 and a<=1364:
                i.color("yellow")
                x=i.xcor()
                y=i.ycor()
                print("a=",a)
                print("x=",x)
                print("y=",y)


h.mainloop()
