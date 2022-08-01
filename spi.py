from turtle import Turtle,Screen
a=Turtle()
h=Screen()
a.turtlesize(2)
b=300
altezza=b/2
k=(altezza**2+altezza**2)**(1/2)
#a.pencolor("blue")
#a.width(2)
a.begin_fill()
a.color("orange")
a.width(2)
i=0
for i in range(0,2):
#while True:
#while i <=1:
    a.left(45)
    a.forward(k)
    a.right(90)
    a.forward(k)
    a.right(135)
    a.forward(b)
    a.right(90)
    a.left(45)
    a.forward(k)
    a.right(90)
    a.forward(k)
    a.right(135)
    a.forward(b)
    a.right(90)
#break
#i=i+1
#print(i)
a.end_fill()
h.mainloop()
