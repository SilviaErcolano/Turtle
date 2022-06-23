from turtle import *
t=Turtle()
s=Screen()
t.width(15)
t.color("light green")
t.speed("fastest")
for _ in range(0,37):
    #t.right(40)
    t.begin_fill()
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.left(60)
    t.end_fill()

    if _ in range (0,11):
      t.color("light green")
    elif _ in range(10,23):
      t.color("red")
    elif _ in range(23,37):
      t.color("orange")
s.mainloop()