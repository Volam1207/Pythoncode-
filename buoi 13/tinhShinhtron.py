#import thư viện 
import math
import turtle 
#tinh dien tich
def tinhdientich(r):
    s = math.pi*r*r
    return s
#ve hinh tron
def ve(r):
    t =turtle.Turtle()
    #t.hideturtle
    t.pencolor('red')
    t.fillcolor('black')
    t.circle(r)
#co the de hai ham chung với nhau 
#ham to mau
def to(r):
    t =turtle.Turtle()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    turtle.done()

bk =float(input("Nhap ban kinh hinh tron: "))
S = tinhdientich(bk)
print("dien tich hinh tron la: ", S )
ve(S)
to(S)