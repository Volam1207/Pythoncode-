#input cd,cr
import math
CD = float(input("Nhap chieu dai: ") )
CR = float(input("Nhap chieu rong: ") )

#process: tinh cv, tinh dien tich
CV = CD * CR
S = (CD + CR) *2

#in ra: CV,DT
print("Chu vi hinh chu nhat la: ",CV)
print("dien tich hinh chu nhat la: ",CD)
#ve hinh chu nhat 
import turtle
t = turtle.Turtle()
t.fillcolor("purple")
t.begin_fill()
t.forward(CD)
t.right(90)
t.forward(CR)
t.right(90)
t.forward(CD)
t.right(90)
t.forward(CR)
t.end_fill() #end to mau
turtle.done()
