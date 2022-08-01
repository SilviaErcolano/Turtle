from turtle import *
o=Turtle()
m=Screen()
o.turtlesize(0.5)
o.penup()
o.goto(100,300)
o.pendown()
o.color("blue")
o.speed("fastest")
#o.color("yellow")
#o.begin_fill()
#spiralecontorno
for i in range(80):
    o.width(2)
    o.right(38)
    o.forward(200)
    if i in range(0,10):
        o.color("blue")
    elif i in range(10,20):
        o.color("red")
    elif i in range(20,30):
        o.color("green")
    elif i in range(30,40):
        o.color("purple")
    elif i in range(40,50):
        o.color("brown")
    elif i in range(50,60):
        o.color("pink")
    elif i in range(60,70):
        o.color("yellow")
    elif i in range(70,80):
        o.color("orange")
#o.color("purple")
#fiore 1
o.penup()
o.goto(55,200)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("orange")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("yellow")
    #o.right(30)
o.color("magenta")
#fiore 2
o.penup()
o.goto(-55,200)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("magenta")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("purple")
o.color("light blue")
#fiore 3
o.penup()
o.goto(190,90)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("light blue")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("blue")
o.color("green")
#fiore 4
o.penup()
o.goto(55,90)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("green")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("red")
#fiore 5
o.color("brown")
o.penup()
o.goto(-55,90)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("brown")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("black")
#fiore 6
o.color("pink")
o.penup()
o.goto(-190,90)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("pink")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("light green")
#fiore 7
o.color("yellow")
o.penup()
o.goto(190,-20)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("yellow")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("grey")
#fiore 8
o.color("orange")
o.penup()
o.goto(55,-20)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("orange")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("red")
#fiore 9
o.color("light green")
o.penup()
o.goto(-55,-20)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("light green")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("green")
#fiore 10
o.color("brown")
o.penup()
o.goto(-190,-20)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("brown")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("magenta")
#fiore 11
o.color("black")
o.penup()
o.goto(190,-130)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("black")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("purple")
#fiore 12
o.color("yellow")
o.penup()
o.goto(55,-130)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("yellow")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("green")
#fiore 13
o.color("orange")
o.penup()
o.goto(-55,-130)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("orange")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("grey")
#fiore 14
o.color("light blue")
o.penup()
o.goto(-190,-130)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("light blue")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("magenta")
#fiore 15
o.color("blue")
o.penup()
o.goto(0,-225)
o.pendown()
for i in range(0,13):
    o.right(45)
    o.circle(radius=-40,extent=80)
    o.right(100)
    o.circle(radius=-40,extent=80)
    if i in range(0,1) or i in range(2,3) or i in range(4,5) or i in range(6,7) or i in range(8,9) or i in range(10,11):
        o.color("blue")
    elif i in range(1,2) or i in range(3,4) or i in range(5,6) or i in range(7,8) or i in range(9,10) or i in range(12,13):
        o.color("black")
m.mainloop()
