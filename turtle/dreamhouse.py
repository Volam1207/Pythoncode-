import turtle 

#Chọn màu nền
turtle.bgcolor("#ffe7bc")

#khởi tạo con con trỏ
t = turtle.Turtle()
t.pensize(3)

# dùng biến 
# Định nghĩa biến cho tọa độ bắt đầu
x = -150 #tự cho
y = -150 #tự cho

# Định nghĩa biến cho trạng thái bút vẽ
pen_state = "penup"


# Di chuyển rùa đến vị trí bắt đầu
t.penup()
t.goto(x,y)

#Vẽ ngôi nhà 
# Tô màu và vẽ hình
#vẽ mái
t.pendown()
t.fillcolor("#385a7c")
t.begin_fill()
t.forward(300)
t.left(150)
t.forward(173.22)
t.left(60)
t.forward(173.22)
t.end_fill()

#vẽ thân nhà 
# Định nghĩa biến cho chiều rộng thân nhà
w = 200
# Định nghĩa biến cho chiều cao thân nhà
h = 240
# Vẽ thân nhà
#di chuột 
t.left(150) 
t.forward(30)
t.right(90)

#chỉnh màu 
t.fillcolor("#4dbedf")
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h)
t.left(90)
t.forward(w)
t.end_fill()

#vẽ cửa chính 
cao = 80
rong = 100
t.penup()
t.backward(200)
t.left(90)
t.pendown()
t.fillcolor("#385a7c")
t.begin_fill()
t.forward(cao)
t.right(90)
t.forward(rong)
t.left(90)
t.forward(cao)
t.left(90)
t.forward(rong)
t.end_fill()

# Định nghĩa biến cho chiều rộng cửa sổ
window_width = 50

# Vẽ cửa sổ trái
window_x_left = -50
t.penup()
t.goto(window_x_left, -170)
t.pendown()
t.fillcolor("#385a7c")
t.begin_fill()
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.end_fill()

# Vẽ cửa sổ phải
window_x_right = 50
t.penup()
t.goto(window_x_right, -170)
t.pendown()
t.fillcolor("#385a7c")
t.begin_fill()
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.right(90)
t.forward(window_width)
t.end_fill()
turtle.done()