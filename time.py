# Time
from turtle import Turtle, Screen
tartaruga = Turtle()
sfondo = Screen()
sfondo.bgcolor("pink")
tartaruga.penup()
tartaruga.goto(-500,-40)
tartaruga.turtlesize(0.5)
tartaruga.pendown()

for i in range(0,11):
    tartaruga.color("blue")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)

for i in range(11, 21):
    tartaruga.color("brown")

    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)

for i in range(21, 31):
    tartaruga.color("green")

    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)

for i in range(31, 41):
    tartaruga.color("black")

    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(41, 51):
    tartaruga.color("red")

    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(51, 61):
    tartaruga.color("purple")

    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    #tartaruga.forward(100)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
tartaruga.penup()
tartaruga.goto(120,-120)
#tartaruga.pendown()
for i in range(61,72):
    tartaruga.color("blue")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(72,81):
    tartaruga.color("brown")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(81,91):
    tartaruga.color("green")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(91,101):
    tartaruga.color("black")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(101, 111):
    tartaruga.color("red")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)
for i in range(111, 121):
    tartaruga.color("purple")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"),)

    tartaruga.right(45)
    tartaruga.circle(radius=150,extent=200)

tartaruga.penup()
tartaruga.goto(450,-40)
tartaruga.pendown()

for i in range(121,132):
        tartaruga.color("blue")
        tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
        tartaruga.right(45)
        tartaruga.circle(radius=150, extent=200)
for i in range(132,142):
    tartaruga.color("brown")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150, extent=200)
for i in range(142, 152):
    tartaruga.color("green")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150, extent=200)
for i in range(152, 162):
    tartaruga.color("black")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150, extent=200)
for i in range(162, 172):
    tartaruga.color("red")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))

    tartaruga.right(45)
    tartaruga.circle(radius=150, extent=200)
for i in range(172, 182):
    tartaruga.color("purple")
    tartaruga.write(i,move=False,align='left',font=("Comic Sans",8,"bold"))
    tartaruga.right(45)
    tartaruga.circle(radius=150, extent=200)
sfondo.mainloop()
