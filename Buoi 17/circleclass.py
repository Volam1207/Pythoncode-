import turtle 
import math 
#xây dựng lớp circle 
class Circle:
  def __init__(self,r,x,y):
    # r : Bán kính 
    # x :hoành độ 
    # y : Tung độ 
    self.r = r 
    self.x = x 
    self.y = y
#Hàm vẽ hình tròn 
  def draw(self):
   t =turtle.Turtle()
   t.hideturtle()
   t.color("Green" )
   t.begin_fill()
   t.penup()
   t.goto(self.x,self.y)
   t.pendown()
   t.circle(self.r)
   t.end_fill()
   turtle.done()

 #Tinh dien tich hinh tron
  def tinhdt(self):
   return math.pi * self.r **2
 #tinh chu vi hinh tron 
  def tinhcv(self):
   return 2 * math.pi * self.r

#thuc thi ve hinh tron
C = Circle(80,100,100)
C.draw()
print("Dien tich hinh tron la: ", C.tinhdt())
print("Chu vi hinh tron la: ", C.tinhcv())

   