import turtle

# Hàm thiết lập màu nền
def set_background_color(color):
  turtle.bgcolor(color)

# Hàm thiết lập rùa
def create_turtle():
  t = turtle.Turtle()
  t.pensize(3)
  t.speed(100)
  return t

# Hàm vẽ hình tam giác
def draw_triangle(t, length, angle1, angle2):
  t.forward(length)
  t.left(angle1)
  t.forward(length)
  t.left(angle2)
  t.forward(length)

# Hàm vẽ hình vuông
def draw_square(t, side_length):
  for _ in range(4):
    t.forward(side_length)
    t.left(90)

# Hàm vẽ cửa sổ
def draw_window(t, x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.fillcolor(color)
  t.begin_fill()
  draw_square(t, 50)
  t.end_fill()

# Hàm vẽ tán cây
def draw_tree_crown(t, x, y, color):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.fillcolor(color)
  t.begin_fill()
  draw_triangle(t, 100, 150, 60)
  t.right(150)
  t.forward(250)
  t.end_fill()

# Hàm vẽ mặt trời
def draw_sun(t, x, y, radius):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.fillcolor("red")
  t.begin_fill()
  t.circle(radius, 360)
  t.end_fill()

# Hàm vẽ tia nắng
def draw_sunbeam(t, length):
  t.pencolor("red")
  t.right(90)
  t.forward(length)
  t.backward(length)
  t.left(90)
  t.circle(60, 45)

# Khởi tạo màn hình
set_background_color("#ffe7bc")

# Khởi tạo rùa
t = create_turtle()

# Vẽ mái nhà
t.penup()
t.goto(150, 150)
t.pendown()
t.fillcolor("#2f4f4f")
t.begin_fill()
draw_triangle(t, 300, 150, 60)
t.end_fill()

# Thân nhà
t.left(150)
t.forward(40)
t.right(90)

t.fillcolor("#cd853f")
t.begin_fill()
draw_square(t, 200)
t.end_fill()

# Vẽ cửa chính
t.left(90)
t.forward(200)
t.left(90)
t.forward(80)
t.left(90)

t.fillcolor("#d8bfd8")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(45)
t.right(90)
t.forward(100)
t.end_fill()

# Vẽ cửa sổ
draw_window(t, 250, 80, "#d8bfd8")
draw_window(t, 330, 80, "#d8bfd8")

# Vẽ thân cây
t.penup()
t.goto(33, 80)
t.pendown()
t.right(90)
t.fillcolor("#86563c")
t.begin_fill()
draw_square(t, 50)
t.end_fill()

# Vẽ tán cây
draw_tree_crown(t, 30, 153, "#4caf50")
draw_tree_crown(t, 30, 229, "#4caf")
turtle.done()