import turtle
t = turtle.Turtle()
#dat ban kinh 
r = 10
#dung vong lap
i = 100
for i in range(200):
    #180 là góc ở tâm, sau đó bán kinh tự + thêm 10 để thành xoắn ốc 
    t.circle(r,180)
    r += 10
    
turtle.done()
