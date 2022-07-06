from turtle import *
t=Turtle()
s=Screen()
s.bgcolor("black")
for i in range(0,36):
    #t.begin_fill()
    t.color("yellow")
    t.right(30)
    t.circle(radius=100,extent=100)
    t.left(120)
    t.circle(radius=100, extent=100)
    #t.fillcolor("purple")
    #t.end_fill()
s.mainloop()