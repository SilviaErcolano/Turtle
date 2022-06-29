from turtle import *
o=Turtle()
s=Screen()
""""
for i in range(10):
    o.width("2")
    o.color("yellow")
    o.left(135)
    o.forward(80)
    o.end_fill()
"""""
""""
o.color("pink")
o.width(2)
o.penup()
o.goto(0,-100)
o.pendown()
#o.speed(10)
"""
""""
for i in range(0,60):
    o.left(43)
    o.circle(radius=100,extent=100*3.14*2)
    if i in range(0,10):
        o.color("pink")
    if i in range(10,20):
        o.color("orange")
    if i in range(20,30):
        o.color("red")
    if i in range(30,40):
         o.color("green")
    if i in range(40,50):
        o.color("purple")
    if  i in range(50,60):
        o.color("brown")
"""
""""
for i in range(0,60):
    o.left(38)
    o.circle(radius=100,extent=100*3.14*2)
    if i in range(0,10):
        o.color("pink")
    if i in range(10,20):
        o.color("orange")
    if i in range(20,30):
        o.color("red")
    if i in range(30,40):
         o.color("green")
    if i in range(40,50):
        o.color("purple")
    if  i in range(50,60):
        o.color("brown")
"""""
""""
for i in range(0,60):
    o.left(50)
    o.circle(radius=100,extent=100*3.14*2)
    if i in range(0,10):
        o.color("pink")
    elif i in range(10,20):
        o.color("orange")
    elif i in range(20,30):
        o.color("red")
    elif i in range(30,40):
         o.color("green")
    elif i in range(40,50):
        o.color("purple")
    elif  i in range(50,60):
        o.color("brown")
"""""
""""
for i in range(0,100):
    if i in range (0,30):
        o.color("yellow")
        o.right(45)
        o.forward(150)
        o.left(200)
        """
""""
o.penup()
o.goto(0,100)
o.pendown()
for i in range(0,12):
    o.color("orange")
    o.right(30)
    o.forward(100)
"""
""""
for i in range(0,6):
    o.forward(50)
    o.right(60)
    o.forward(50)
    o.left(120)
o.end_fill()
"""
s.mainloop()