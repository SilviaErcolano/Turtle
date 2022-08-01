from turtle import *
t=Turtle()
s=Screen()
s.bgcolor("pink")
t.color("purple")
t.speed(10)
for i in range(0,19):
#for i in range (0,9):
    #t.begin_fill()
    t.right(120)
    t.circle(radius=200,extent=100)
    t.left(80)
    t.circle(radius=200, extent=100)
    #t.end_fill()

    if i in range(0, 9):
        t.color("purple")
    elif i in range(9, 19):
        t.color("yellow")

s.mainloop()