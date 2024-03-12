import math

#input R
R = float(input("Nhap vao duong kinh: "))
#Process S = ap dung cong thuc tinh dien tich hinh tron
S = math.pi * R * R
#Display S 
print("dien tich hinh tron la:",S)
#su dung thu vien math
import turtle
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(R)
turtle.end_fill()
turtle.done()