from turtle import *
s=Turtle()
x=Screen()
#a=int()
a=120
b=150
y=(a**2+b**2)**(1/2)

s.left(45)
#for i in range(0,5):
for i in range(0,1):
     s.begin_fill()
     s.color("red")
     s.forward(y)
     s.right(90)
     s.forward(y)
     s.right(135)
     s.forward(2 * b)
     s.right(45)
     s.end_fill()
for i in range(1,2):
         s.begin_fill()
         s.color("green")
         s.forward(y)
         s.right(90)
         s.forward(y)
         s.right(135)
         s.forward(2 * b)
         s.right(45)
         s.end_fill()
for i in range(2,3):
             s.begin_fill()
             s.color("yellow")
             s.forward(y)
             s.right(90)
             s.forward(y)
             s.right(135)
             s.forward(2 * b)
             s.right(45)
             s.end_fill()
for i in range(4,5):
                 s.begin_fill()
                 s.color("blue")
                 s.forward(y)
                 s.right(90)
                 s.forward(y)
                 s.right(135)
                 s.forward(2 * b)
                 s.right(45)
                 s.end_fill()



x.mainloop()