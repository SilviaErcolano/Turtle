from turtle import Turtle,Screen
t=Turtle()
s=Screen()
s.bgcolor("magenta")
i=0
t.width(5)
t.color("light green")
#for i in range(0,8):
while i<=7:
    i=i+1
    t.circle(radius=120,extent=360)
    t.right(40)
    t.circle(radius=120,extent=360)
    t.end_fill()


s.mainloop()