# lay cong cu ve
import turtle 
# lay ngoi viet 
t = turtle.Turtle()
#nhacngoi 
t.penup()
#dichuyendenchove
t.goto(-200,-200)
#de ngoi vie xuong
t.pendown()
#vehinhvuong
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

#xoay con tro ve tam giac
t.left(45)
t.forward(80)
#xoay con tro ve tam gia 
t.right(97)
t.forward(80) 

#ve hinh tron 
t.penup()
t.goto(200,200)
t.pendown()
t.circle(40)

turtle.done()