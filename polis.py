from turtle import *
#polis

p=Turtle()
s=Screen()
p.width(20)
p.color("red")
p.forward(50)
p.left(45)
p.color("brown")
p.circle(radius=40,extent=180)
p.left(45)
p.color("orange")
p.forward(155)
p.color("yellow")
p.circle(radius=23)
p.circle(radius=23,extent=72.25663103)
p.left(20)
#p.left(90)
p.forward(40)
p.color("pink")
p.left(90)
p.forward(70)
p.backward(70)
p.right(90)
p.forward(15)
p.color("purple")
p.left(90)
p.forward(30)
p.backward(30)
p.right(90)
p.color("green")
#p.forward(30)
p.circle(radius=35,extent=1/4*(2*3.14*35))
p.right(35)
p.left(50)
p.circle(radius=35,extent=1/4*(2*3.14*35))
p.right(80)
p.forward(35)
s.mainloop()