import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
c1=140
c2=140
ip=(c1**2+c2**2)**(1/2)
a=0
#for _ in (0,41):
#while True:
while a<=40:
    a=a+1
    print("a=",a)
    t.color("yellow")
    t.left(45)
    t.forward(ip)
    t.right(90)
    t.forward(ip)
    t.right(90)
    t.forward(ip)
    t.right(90)
    t.forward(ip)
    t.right(5)
    """"
    t.left(30)
    t.forward(50)
    t.left(10)
    t.forward(50)
    t.left(120)
    t.forward(100)
    t.right(120)
    t.forward(200)
    """
s.mainloop()