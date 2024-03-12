import turtle
wn = turtle.Screen() #setup cho background
wn.bgcolor("black") #mau cho background
wn.title("Star") #title cho rua
myPen = turtle.Turtle()
myPen.speed(0) #toc doc
myPen.color("green")
for j in range (1,100):
    for i in range (1,6): #dong nay la ve ngoi sao
      myPen.left(144)
      myPen.forward(200)
    myPen.left(5)   
turtle.done()