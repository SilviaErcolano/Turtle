from turtle import Turtle,Screen
t=Turtle()
s=Screen()
a=int()
t.left(180)
t.speed("fastest")
for a in range(0,801):
    if a in range(0,101):
        t.color("orange")
    elif a in range(101,201):
        t.color("green")
    elif a in range(201,301):
        t.color("yellow")
    elif a in range(301,401):
        t.color("red")
    elif a in range(401,501):
        t.color("purple")
    elif a in range(501,601):
        t.color("pink")
    elif a in range(601,701):
        t.color("brown")
    elif a in range(701,801):
        t.color("light green")


    t.forward(a)
    t.right(135)
    i = (a ** 2 + a ** 2) ** (1 / 2)
    t.forward(i)
    t.right(90)
    t.forward(i)
    t.right(135)
    t.forward(2 * a)
    print("a=", a)
    t.right(135)

t.speed("fastest")
s.mainloop()