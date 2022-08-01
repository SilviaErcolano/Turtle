from turtle import *
y=Turtle()
h=Screen()
y.speed("fastest")
while True:
    y.right(5)
    y.circle(radius=60, extent=1/6*2*3.14*100,steps=10)
    y.left(2)
    y.circle(radius=80,extent=1/6*2*3.14*180,steps=20)
    y.left(2)
    y.circle(radius=100,extent=1/5*2*3.14*200,steps=30)
    #break
    #h.exitonclick()
