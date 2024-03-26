import turtle 
turtle.bgcolor("#ffe7bc")
#Khơi tạo con trỏ 
t = turtle.Turtle()
#thiết lập kích thước và tốc độ
t.pensize(3)
t.speed(100)
#vẽ mái nhà 
t.penup() #nhấc con trỏ
t.goto(150,150)
t.pendown()
t.fillcolor("#2f4f4f")
t.begin_fill()
#ve tam giac 
t.forward(300)
t.left(150)#xoay trái 150 độ
t.forward(173.22)
t.left(60)#xoay trái 150 độ
t.forward(173.22)
t.end_fill() #dừng tô

#than nha ve bằng hình vuông
t.left(150)
t.forward(40)
t.right(90)

t.fillcolor("#cd853f")
t.begin_fill()
#ve hinh vuong
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.end_fill()
 
#ve cua chinh 
#t.backward() sẽ di chuyển rùa một khoảng cách nhất định theo hướng ngược lại so với hướng hiện tại.
#di chuột để vẽ cửa 
t.left(90)
t.forward(200)
t.left(90)
t.forward(80)
t.left(90)
#vẽ cửa
t.fillcolor("#d8bfd8")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(45)
t.right(90)
t.forward(100)
t.end_fill()

#ve cua so phải 
t.penup()
t.goto(250,80)
t.pendown()
t.fillcolor("#d8bfd8")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()

#ve cửa sổ trái 
#ve cua so phải 
t.penup()
t.goto(330,80)
t.pendown()
t.fillcolor("#d8bfd8")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()

#ve cây
#than cay
t.penup()
t.goto(33,80)
t.pendown
t.right(90)
t.fillcolor("#86563c")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.right(90)
t.forward(150)
t.end_fill()
#tancay
#tán cây thứ 1 
t.left(90)
t.fillcolor("#4caf50")
t.begin_fill()
#ve tam giác

t.forward(100)
t.right(150)
t.forward(144.34)
t.right(60)
t.forward(144.34)
t.right(150)
t.forward(250)
t.end_fill()

#tán thứ 2 
t.penup()
t.goto(30,153)
t.pendown()
t.fillcolor("#4caf50")
t.begin_fill()
t.forward(100)
t.right(150)
t.forward(144.34)
t.right(60)
t.forward(144.34)
t.right(150)
t.forward(250)
t.end_fill()
t.penup()

#tan thu 3
#tán thứ 2 
t.penup()
t.goto(30,229)
t.pendown()
t.fillcolor("#4caf50")
t.begin_fill()
t.forward(100)
t.right(150)
t.forward(144.34)
t.right(60)
t.forward(144.34)
t.right(150)
t.forward(250)
t.end_fill()
t.penup()

#vemattroi 
t.goto(400,350)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(60,360)
t.end_fill()


#ve tia nắng
t.pencolor("red")
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)

t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(60,45)
turtle.done()