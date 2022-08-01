from turtle import *
t=Turtle()
s=Screen()
s.bgcolor("purple")
t.left(90)
t.speed("fastest")
t.width(1)
for i in range(0,771):
    if i>=0 and i<=100 or i>200 and i<=300 or i>400 and i<=500 or i>600 and i<=700 :
        t.color("magenta")
        t.circle(radius=-i,extent=180)
        print("imagenta=",i)
    elif i>100 and i<=200 or i>300 and i<=400 or i>500 and i<=600 or i>700 and i<=770:
        t.color("yellow")
        t.circle(radius=-i,extent=180)
        print("iyellow=", i)

""""
for i in range(0,771):
    if i>=0 and i<=100 or i>=200 and i<=300 or i>=400 and i<=500 or i>=600 and i<=700:
        t.color("magenta")
        t.circle(radius=-i,extent=180)
        print("imagenta=",i)
    elif i >=100 and i<=200 or i>=300 and i<=400 or i>=500 and i<=600 or i>=700 and i<=770:
        t.color("yellow")
        t.circle(radius=-i, extent=180)
        print("iyellow=", i)
"""
s.mainloop()
