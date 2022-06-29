from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.penup()
t.goto(-150,200) #A
t.pendown()
xa=-150
ya=200
print("xa=",xa,"ya=",ya)
t.width(2)
#pixel 1
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 2
t.penup()
t.goto(-150+40,200) #B
t.pendown()
xb=-150+40
yb=200
print("xb=",xb,"yb=",yb)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 3
t.penup()
t.goto(-150+40+80,200) #C
t.pendown()
xc=-150+40+80
yc=200
print("xc=",xc,"yc=",yc)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 4
t.penup()
t.goto(-150+40+80+40,200) #D
t.pendown()
xd=-150+40+80+40
yd=200
print("xd=",xd,"yd=",yd)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 5
t.penup()
t.goto(-150-40,200-40) #E
t.pendown()
xe=-150-40
ye=200-40
print("xe=",xe,"ye=",ye)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 6
t.penup()
t.goto(-150-40+40,200-40) #F
t.pendown()
xf=-150-40+40
yf=200-40
print("xf=",xf,"yf=",yf)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 7
t.penup()
t.goto(-150-40+40+40,200-40) #G
t.pendown()
xg=-150-40+40+40
yg=200-40
print("xg=",xg,"yg=",yg)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("red")
t.end_fill()
#pixel 8
t.penup()
t.goto(-150-40+40+40+40,200-40) #H
t.pendown()
xh=-150-40+40+40+40
yh=200-40
print("xh=",xh,"yh",yh)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("red")
t.end_fill()
#pixel 9
t.penup()
t.goto(-150-40+40+40+40+40,200-40) #I
t.pendown()
xi=-150-40+40+40+40+40
yi=200-40
print("xi=",xi,"yi=",yi)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("red")
t.end_fill()
#pixel 10
t.penup()
t.goto(-150-40+40+40+40+40+40,200-40) #L
t.pendown()
xl=-150-40+40+40+40+40+40
yl=200-40
print("xl=",xl,"yl=",yl)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 11
t.penup()
t.goto(-150-40+40+40+40+40+40+40,200-40) #M
t.pendown()
xm=-150-40+40+40+40+40+40+40
ym=200-40
print("xm=",xm,"ym=",ym)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 12
t.penup()
t.goto(-150-40,200-40-40) #N
t.pendown()
xn=-150-40
yn=200-40-40
print("xn=",xn,"yn=",yn)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 13
t.penup()
t.goto(-150-40+40,200-40-40) #0
t.pendown()
xo=-150-40+40
yo=200-40-40
print("xo=",xo,"yo=",yo)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.end_fill()
#pixel 14
t.penup()
t.goto(-150-40+40+40,200-40-40) #P
t.pendown()
xp=-150-40+40+40
yp=200-40-40
print("xp=",xp,"yp=",yp)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("orange")
t.end_fill()
#pixel 15
t.penup()
t.goto(-150-40+40+40+40,200-40-40) #Q
t.pendown()
xq=-150-40+40+40+40
yq=200-40-40
print("xq=",xq,"yq=",yq)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("orange")
t.end_fill()
#pixel 16
t.penup()
t.goto(-150-40+40+40+40+40,200-40-40) #R
t.pendown()
xr=-150-40+40+40+40+40
yr=200-40-40
print("xr=",xr,"yr=",yr)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("orange")
t.end_fill()
#pixel 17
t.penup()
t.goto(-150-40+40+40+40+40+40,200-40-40) #S
t.pendown()
xs=-150-40+40+40+40+40+40
ys=200-40-40
print("xs=",xs,"ys=",ys)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("red")
t.end_fill()
#pixel 18
t.penup()
t.goto(-150-40+40+40+40+40+40+40,200-40-40) #T
t.pendown()
xt=-150-40+40+40+40+40+40+40
yt=200-40-40
print("xt=",xt,"yt=",yt)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
#pixel 19
t.penup()
t.goto(-150,200-40-40-40) #U
t.pendown()
xu=-150
yu=200-40-40-40
print("xu=",xu,"yu=",yu)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.end_fill()
#pixel 20
t.penup()
t.goto(-150+40,200-40-40-40) #V
t.pendown()
xv=-150+40
yv=200-40-40-40
print("xv=",xv,"yv=",yv)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("yellow")
t.end_fill()
#pixel 21
t.penup()
t.goto(-150+40+40,200-40-40-40) #X
t.pendown()
xx=-150+40+40
yx=200-40-40-40
print("xx=",xx,"yv=",yx)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("yellow")
t.end_fill()
#pixel 22
t.penup()
t.goto(-150+40+40+40,200-40-40-40) #Y
t.pendown()
xy=-150+40+40+40
yy=200-40-40-40
print("xy=",xy,"yy=",yy)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("yellow")
t.end_fill()
#pixel 23
t.penup()
t.goto(-150+40+40+40+40,200-40-40-40) #Z
t.pendown()
xz=-150+40+40+40+40
yz=200-40-40-40
print("xz=",xz,"yz=",yz)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("red")
t.end_fill()
# pixel 24
t.penup()
t.goto(-150+40,200-40-40-40-40) #Z1
t.pendown()
xz1=-150+40
yz1=200-40-40-40-40
print("xz1=",xz1,"yz1=",yz1)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("light green")
t.end_fill()
#pixel 25
t.penup()
t.goto(-150+40+40,200-40-40-40-40) #Z2
t.pendown()
xz2=-150+40+40
yz2=200-40-40-40-40
print("xz2=",xz2,"yz2=",yz2)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("light green")
t.end_fill()
#pixel 26
t.penup()
t.goto(-150+40+40+40,200-40-40-40-40) #Z3
t.pendown()
xz3=-150+40+40+40
yz3=200-40-40-40-40
print("xz3=",xz3,"yz3=",yz3)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("light green")
t.end_fill()
#pixel 27
t.penup()
t.goto(-150+40+40,200-40-40-40-40-40) #Z4
t.pendown()
xz4=-150+40+40
yz4=200-40-40-40-40-40
print("xz4=",xz4,"yz4=",yz4)
t.begin_fill()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.fillcolor("light blue")
t.end_fill()
s.mainloop()

