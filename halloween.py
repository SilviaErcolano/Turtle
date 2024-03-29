from turtle import *

t = Turtle()
s = Screen()
s.bgcolor("black")
t.penup()
t.goto(-660, 300)
t.pendown()
for i in range(0, 9):
    print("i=", i)
    t.color("white")
    t.begin_fill()
    t.left(90)
    t.circle(radius=-40, extent=180)
    t.forward(50)
    t.speed("fastest")
    # 7parti
    unite = 80 / 7
    print("unità=", unite)
    t.circle(radius=-unite / 2, extent=180)
    t.circle(radius=unite / 2, extent=180)
    t.circle(radius=-unite / 2, extent=180)
    t.circle(radius=unite / 2, extent=180)
    t.circle(radius=-unite / 2, extent=180)
    t.circle(radius=unite / 2, extent=180)
    t.circle(radius=-unite / 2, extent=180)
    t.forward(50)
    t.end_fill()
    xinizio = t.xcor()
    yinizio = t.ycor()
    print("xinizio=", xinizio, "yinizio=", yinizio)
    # occhio1
    t.color("black")
    t.color("yellow")
    t.penup()
    t.goto(xinizio + 10, yinizio)
    t.pendown()
    t.begin_fill()
    t.circle(radius=-10, extent=360)
    t.end_fill()
    xinizioocchio = xinizio + 10
    yinizioocchio = yinizio
    print("xinizioocchio=", xinizioocchio, "yinizioocchio=", yinizioocchio)
    # pupilla
    t.penup()
    t.goto(xinizioocchio + 5, yinizioocchio)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(radius=-5, extent=360)
    t.end_fill()
    # occhio2
    t.penup()
    t.goto(xinizioocchio + 40, yinizioocchio)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius=-10, extent=360)
    t.end_fill()
    xsecondoocchio = t.xcor()
    ysecondoocchio = t.ycor()
    print("xsecondoocchio=", xsecondoocchio, "ysecondoocchio=", ysecondoocchio)
    # pupilla2
    t.penup()
    t.goto(xsecondoocchio + 5, ysecondoocchio)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(radius=-5, extent=360)
    t.end_fill()
    # bocca
    xestremopupilla = t.xcor()
    yestremopupilla = t.ycor()
    print("xestremopupilla=", xestremopupilla, "yestremopupilla=", yestremopupilla)
    t.penup()
    t.goto(xestremopupilla - 5, yestremopupilla - 30)
    t.pendown()
    t.begin_fill()
    t.circle(radius=10, extent=360)
    t.fillcolor("red")
    t.end_fill()
    xestremobocca = t.xcor()
    yestremobocca = t.ycor()
    print("xestremobocca=", xestremobocca, "yestremobocca=", yestremobocca)
    t.penup()
    t.goto(xestremobocca - 50, yestremobocca + 30)
    t.pendown()
    # spostamentosecondofantasma
    xbase = t.xcor()
    ybase = t.ycor()
    print("xbase=", xbase, "ybase=", ybase)
    t.right(90)
    t.penup()
    t.goto(xbase + 150, ybase)
    t.pendown()

# zucca
t.penup()
t.goto(-670, 180)
t.pendown()
for i in range(0, 9):
    t.begin_fill()
    t.color("orange")
    r1 = 45 / 2
    r2 = 10 / 2
    t.left(90)
    t.circle(radius=-r1, extent=180)
    t.circle(radius=r2, extent=180)
    t.circle(radius=-r1, extent=180)
    diametro = 2 * r1 + 2 * r1 + 2 * r2
    t.circle(radius=-diametro / 2, extent=180)
    t.end_fill()
    t.circle(radius=-r1, extent=180)
    t.begin_fill()
    t.color("green")
    t.circle(radius=r2, extent=180)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.end_fill()
    # occhi
    # occhio1
    xfinegambo = t.xcor()
    yfinegambo = t.ycor()
    t.penup()
    t.goto(xfinegambo - r1, yfinegambo - 10)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.left(90)
    # triangolo isoscele
    a = 13
    m = (a ** 2 + a ** 2) ** (1 / 2)
    t.forward(a)
    t.backward(a)
    t.left(90)
    t.forward(a)
    t.right(135)
    t.forward(m)
    t.end_fill()
    t.begin_fill()
    t.backward(m)
    t.right(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(135)
    t.forward(m)
    t.end_fill()
    # occhio2
    t.penup()
    t.goto(xfinegambo + r2 + r1, yfinegambo - 10)
    t.pendown()
    t.begin_fill()
    t.right(45)
    t.forward(a)
    t.backward(a)
    t.left(90)
    t.forward(a)
    t.right(135)
    t.forward(m)
    t.end_fill()
    t.begin_fill()
    t.backward(m)
    t.right(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(135)
    t.forward(m)
    t.end_fill()
    t.right(180)
    t.forward(m)
    t.left(45)
    xfineocchio = t.xcor()
    yfineocchio = t.ycor()
    print("xfineocchio=", xfineocchio, "yfineocchio=", yfineocchio)
    t.penup()
    t.goto(xfineocchio, yfineocchio - 15)
    # naso
    t.pendown()
    t.begin_fill()
    t.right(90)
    anaso = 10
    inaso = (anaso ** 2 + anaso ** 2) ** (1 / 2)
    t.forward(2 * anaso)
    t.right(135)
    t.forward(inaso)
    t.right(90)
    t.forward(inaso)
    t.end_fill()
    xfinebocca = t.xcor()
    yfinebocca = t.ycor()
    print("xfinebocca=", t.xcor(), "yfinebocca=", t.ycor())
    # bocca
    t.penup()
    t.goto(xfinebocca + 10, yfinebocca - 12)
    t.pendown()
    t.begin_fill()
    t.left(180)
    a = 3
    il = (a ** 2 + a ** 2) ** 1 / 2
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.right(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.right(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.right(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.right(90)
    t.forward(il)
    t.left(90)
    t.forward(il)
    t.right(45)
    t.end_fill()
    xestremoboccap = t.xcor()
    yestremoboccap = t.ycor()
    print("xestremobocca=", xestremoboccap, "yestremobocca=", yestremoboccap)
    deltax = -600.4999999999989 + 670
    print(deltax)
    deltay = 143.00000000000088 - 180
    print(deltay)
    t.penup()
    t.goto(xestremoboccap - 69.50000000000114, yestremoboccap + 36.99999999999912)
    t.pendown()
    xbasep = t.xcor()
    ybasep = t.ycor()
    print(xbasep, ybasep)
    t.penup()
    t.goto(xbasep + 150, ybasep)
    t.pendown()
# faccinanightmarebeforechristmas
t.penup()
t.goto(-670, 60)
t.pendown()
for i in range(0, 9):
    xiniziale = t.xcor()
    yiniziale = t.ycor()
    t.pencolor("white")
    t.left(90)
    t.begin_fill()
    t.fillcolor("white")
    t.circle(radius=-50, extent=360)
    t.end_fill()
    # occhio1
    t.penup()
    t.goto(xiniziale + 20, yiniziale + 15)
    t.pendown()
    t.pencolor("black")
    t.begin_fill()
    t.fillcolor("black")
    t.circle(radius=-7, extent=360)
    t.end_fill()
    # occhio2
    t.penup()
    t.goto(xiniziale + 65, yiniziale + 15)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(radius=-7, extent=360)
    print("fineocchio2=", t.xcor())
    t.end_fill()
    # naso
    t.penup()
    t.goto(xiniziale + 44, yiniziale - 5)
    t.pendown()
    t.right(80)
    print("angoloinizioochhio=", t.heading())
    t.begin_fill()
    t.fillcolor("black")
    t.circle(radius=-3, extent=360)
    t.end_fill()
    print(t.heading())
    t.penup()
    t.goto(xiniziale + 55, yiniziale - 5)
    t.pendown()
    # t.left(65)
    print(t.heading())
    t.right(180)
    t.begin_fill()
    t.fillcolor("black")
    t.circle(radius=3, extent=360)
    t.end_fill()
    # bocca
    t.penup()
    t.goto(xiniziale + 20, yiniziale - 15)
    t.pendown()
    t.width(3)
    dist = 59
    raggio = dist / 2
    print(t.heading())
    t.right(10)
    print(t.heading())
    t.left(90)
    t.circle(radius=raggio, extent=180)
    # cuciturebocca
    t.right(180)
    # cucitura1
    # angolo30
    t.circle(radius=-raggio, extent=30)
    print("angoloin=", t.heading())
    t.right(90)
    print("angolopartenza=", t.heading())
    t.circle(radius=-30, extent=20)
    t.right(180)
    t.circle(radius=30, extent=35)
    print(t.heading())
    t.right(180)
    print(t.heading())
    t.circle(radius=-30, extent=15)
    print(t.heading())
    t.left(90)
    print("angolofin=", t.heading())
    # cucitura2
    # angolo60
    t.circle(radius=-raggio, extent=30)
    print("angoloin2=", t.heading())
    t.right(60)
    print("angolopartenza2=", t.heading())
    t.circle(radius=-30, extent=20)
    t.right(180)
    t.circle(radius=30, extent=35)
    t.right(180)
    t.circle(radius=-30, extent=15)
    print(t.heading())
    t.left(60)
    print("angolofinale2=", t.heading())
    # cucitura3
    # angolo3
    # angolo90
    t.circle(radius=-raggio, extent=30)
    print("angoloin3=", t.heading())
    t.right(50)
    print("angolopartenza3=", t.heading())
    t.circle(radius=-30, extent=20)
    t.right(180)
    t.circle(radius=30, extent=35)
    t.right(180)
    t.circle(radius=-30, extent=15)
    print(t.heading())
    t.left(50)
    print("angolofinale3=", t.heading())
    # angolo4
    # 120
    t.circle(radius=-raggio, extent=30)
    print("angoloiniziale4=", t.heading())
    t.right(40)
    print("angolodipartenza4=", t.heading())
    t.circle(radius=-30, extent=20)
    t.right(180)
    t.circle(radius=30, extent=35)
    t.right(180)
    t.circle(radius=-30, extent=15)
    t.left(40)
    print("angolofinale4=", t.heading())
    # cucitura5
    # 150
    t.circle(radius=-raggio, extent=30)
    print("angoloiniziale5=", t.heading())
    t.right(50)
    print("angolodipartenza5=", t.heading())
    t.circle(radius=-raggio, extent=20)
    t.right(180)
    t.circle(radius=30, extent=45)
    t.right(180)
    t.circle(radius=-30, extent=25)
    t.left(50)
    print("angolofinale5=", t.heading())
    t.circle(radius=-raggio, extent=30)
    xfinale = t.xcor()
    yfinale = t.ycor()
    print(xfinale, yfinale)
    deltax = xiniziale - xfinale
    deltay = yiniziale - yfinale
    print(deltax, deltay)
    t.penup()
    t.goto(xfinale + deltax, yfinale + deltay)
    t.pendown()
    t.right(90)
    t.penup()
    t.goto(t.xcor() + 150, t.ycor())
'#Frankestein'
t.penup()
t.goto(-660, -60)
t.pendown()
print(t.heading())
for i in range(0, 9):
    t.color("green")
    t.begin_fill()
    t.left(180)
    t.circle(radius=10, extent=180)
    t.right(90)
    t.forward(30)
    t.circle(radius=45, extent=180)
    t.forward(30)
    t.right(90)
    t.circle(radius=10, extent=180)
    t.right(90)
    t.forward(15)
    t.circle(radius=45, extent=180)
    t.forward(15)
    t.end_fill()
    t.backward(7.5)
    t.color("black")
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.forward(20)
    t.backward(10)
    t.left(90)
    t.forward(18)
    print(t.xcor(), t.ycor())
    t.penup()
    t.goto(t.xcor(), t.ycor() - 9.5)
    t.pendown()
    print("h", t.heading())
    t.circle(radius=-8, extent=180)
    t.right(180)
    t.circle(radius=8, extent=90)
    t.left(90)
    t.circle(radius=-8, extent=40)
    t.right(180)
    print(t.xcor(), t.ycor())
    deltax = -567.142300877491 - (-569.9999999999991)
    deltay = -68.12835554494846 - (-52.499999999996675)
    print(deltax, deltay)
    print(t.xcor() - deltax)
    print(t.ycor() - deltay)
    t.penup()
    t.goto(t.xcor() - deltax, t.ycor() - deltay)
    t.pendown()
    t.setheading(90)
    t.color("green")
    t.forward(7.5)
    t.circle(radius=45, extent=180)
    t.forward(7.5)
    print("v", t.xcor(), t.ycor())
    t.penup()
    t.goto(t.xcor(), t.ycor() - 9.5)
    t.pendown()
    t.color("black")
    t.setheading(0)
    t.right(180)
    t.circle(radius=8, extent=180)
    t.left(180)
    t.circle(radius=-8, extent=90)
    t.right(90)
    t.circle(radius=8, extent=40)
    print(t.xcor(), t.ycor())
    deltax2 = -662.8576991225079 - (-660.0000000000005)
    deltay2 = -68.12835554495189 - (-52.499999999999886)
    print("deltax2", deltax2, "deltay2", deltay2)
    t.penup()
    t.goto(t.xcor() - deltax2, t.ycor() - deltay2)
    t.pendown()
    print(t.xcor(), t.ycor())
    t.penup()
    t.goto(t.xcor() + 18, t.ycor() - 7.5 - 20)
    t.pendown()
    print("h", t.xcor(), t.ycor())
    t.setheading(0)
    t.color("black")
    t.begin_fill()
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.fillcolor("white")
    t.end_fill()
    t.penup()
    t.goto(t.xcor() + 9, t.ycor() - 4.5)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.setheading(0)
    t.begin_fill()
    t.circle(radius=-4.5)
    t.end_fill()
    print(t.xcor(), t.ycor())
    dx = -633.0000000000005 - (-642.0000000000005)
    dy = -84.4999999999999 - (-79.99999999999989)
    print(dx, dy)
    t.penup()
    t.goto(t.xcor() - dx, t.ycor() - dy)
    t.pendown()
    print(t.xcor(), t.ycor())
    t.penup()
    t.goto(t.xcor() + 36, t.ycor())
    t.pendown()
    print("u", t.xcor(), t.ycor())
    t.begin_fill()
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.right(90)
    t.forward(18)
    t.fillcolor("white")
    t.end_fill()
    t.penup()
    t.goto(t.xcor() + 9, t.ycor() - 4.5)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("black")
    t.circle(radius=-4.5)
    t.end_fill()
    print(t.xcor(), t.ycor())
    dux = -597.0000000000005 - (-606.0000000000005)
    duy = -84.49999999999989 - (-79.99999999999989)
    t.penup()
    t.goto(t.xcor() - dx, t.ycor() - dy - 18 - 9)
    t.pendown()
    t.right(90)
    t.circle(radius=-9, extent=180)
    t.right(180)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 28)
    t.pendown()
    t.left(90)
    t.forward(36)
    t.begin_fill()
    t.right(90)
    t.forward(9)
    t.right(90)
    t.forward(18)
    t.right(90)
    t.forward(9)
    t.fillcolor("white")
    t.right(90)
    t.forward(18)
    t.backward(18)
    t.end_fill()
    t.begin_fill()
    t.right(180)
    t.forward(18)
    t.left(90)
    t.forward(9)
    t.left(90)
    t.forward(18)
    t.end_fill()
    t.backward(18)
    t.begin_fill()
    t.right(180)
    t.forward(18)
    t.right(90)
    t.forward(9)
    t.right(90)
    t.forward(18)
    t.fillcolor("white")
    t.end_fill()
    print(t.xcor(), t.ycor())
    deltaxin = -624.0000000000007 - (-660)
    deltayin = -135.0000000000006 - (-60)
    t.penup()
    t.goto(t.xcor() - deltaxin, t.ycor() - deltayin)
    t.pendown()
    print(t.xcor(), t.ycor())
    t.color("green")
    t.left(90)
    t.forward(15)
    t.left(90)
    t.color("grey")
    t.forward(15)
    t.left(90)
    t.begin_fill()
    t.circle(radius=-4)
    t.end_fill()
    t.left(90)
    t.forward(15)
    t.color("green")
    t.left(90)
    t.circle(radius=-45, extent=180)
    t.left(90)
    t.color("grey")
    t.forward(15)
    a = 4
    m = (a ** 2 + a ** 2) ** (1 / 2)
    t.right(135)
    t.forward(m)
    t.backward(m)
    t.right(90)
    t.forward(m)
    print(t.xcor(), t.ycor())
    deltaxcapo = -558.9999999999993 - (-660.0)
    deltaycapo = -40.99999999999564 - (-60.0)
    t.penup()
    t.goto(t.xcor() - deltaxcapo, t.ycor() - deltaycapo)
    t.pendown()
    print(t.xcor(), t.ycor())
    t.setheading(0)
    t.penup()
    t.goto(t.xcor() + 150, t.ycor())
    t.color("green")
    t.pendown()
# cappello
t.penup()
t.goto(-625, -190)
t.pendown()
print(t.heading())
for i in range(0, 9):
    x0 = t.xcor()
    y0 = t.ycor()
    t.begin_fill()
    t.color("purple")
    t.left(90)
    t.circle(radius=-10, extent=180)
    t.left(10)
    print(t.heading())
    t.forward(50)
    print(t.xcor(), t.ycor())
    x1 = t.xcor()
    y1 = t.ycor()
    t.left(180)
    t.forward(50)
    t.right(10)
    t.circle(radius=10, extent=180)
    t.right(10)
    t.forward(50)
    print(t.xcor(), t.ycor())
    x2 = t.xcor()
    y2 = t.ycor()
    t.setheading(360)
    t.right(90)
    dx = x2 - x1
    print(dx)
    t.circle(radius=(-dx / 2), extent=180)
    t.left(10)
    t.forward(50)
    t.right(10)
    t.circle(radius=10, extent=180)
    t.end_fill()
    t.right(10)
    t.forward(50)
    t.setheading(90)
    t.begin_fill()
    t.color("brown")
    t.left(90)
    t.width(10)
    t.forward(dx)
    t.color("purple")
    t.width(1)
    t.right(90)
    t.circle(radius=-12.5, extent=180)
    print(t.xcor(), t.ycor())
    x3 = t.xcor()
    y3 = t.ycor()
    t.left(180)
    t.circle(radius=12.5, extent=180)
    t.right(90)
    t.color("brown")
    t.width(10)
    t.forward(-dx)
    t.right(90)
    t.begin_fill()
    t.color("purple")
    t.width(1)
    t.circle(radius=12.5, extent=180)
    print(t.xcor(), t.ycor())
    x4 = t.xcor()
    y4 = t.ycor()
    ddx = x4 - x3
    t.circle(radius=-ddx / 2, extent=180)
    t.circle(radius=12.5, extent=180)
    t.end_fill()
    xfin = t.xcor()
    yfin = t.ycor()
    dxpuntofinale = xfin - x0
    dypuntofinale = yfin - y0
    t.penup()
    t.goto(t.xcor() - dxpuntofinale, t.ycor() - dypuntofinale)
    t.pendown()
    print(t.xcor(), t.ycor())
    t.setheading(0)
    t.penup()
    t.goto(t.xcor() + 150, t.ycor())
    t.pendown()

s.mainloop()
