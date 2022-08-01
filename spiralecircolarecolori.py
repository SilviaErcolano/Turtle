from turtle import *
t=Turtle()
s=Screen()
s.bgcolor("black")
t.pencolor("red")
t.left(90)
t.speed("fastest")

for i in range(0,771):
    if i in range(0, 101):
        t.color("green")
        t.circle(radius=-i,extent=180)
        print("i=",i)
    elif i in range(101,201):
        t.color("red")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(201,301):
        t.color("pink")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(301,401):
        t.color("brown")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(401, 501):
        t.color("orange")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(501,601):
        t.color("yellow")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(601,701):
        t.color("blue")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(701,771):
        t.color("light green")
        t.circle(radius=-i, extent=180)
        print("i=", i)

""""
    elif i in range(801,901):
        t.color("purple")
        t.circle(radius=-i, extent=180)
        print("i=", i)
    elif i in range(101, 201):
        t.color("light blue")
        t.circle(radius=-i, extent=180)
        print("i=", i)

#if i in range (0,100):
    #t.color("green")

#t.circle(radius=(-i+5), extent=180)
"""
""""

t.circle(radius=-15,extent=180)
t.circle(radius=-20,extent=180)
t.circle(radius=-25,extent=180)
t.circle(radius=-30,extent=180)
t.circle(radius=-35,extent=180)
t.circle(radius=-40,extent=180)
t.circle(radius=-45,extent=180)
"""
#s.mainloop()
