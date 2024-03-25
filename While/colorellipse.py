#import turtle 
import turtle
turtle.bgcolor("black")
t=turtle.Turtle 
 
#hàm vẽ hình elip
def draw(r):
    for i in range(2):
        turtle.circle(r,90)
        turtle.circle(r//2,90)
    
#color
col = ['violet','blue','orange','red','green','orange','purple','yellow','purple','brown','white']

#tạo biến 
dotre = 0
ind = 0
turtle.speed(100)
#tao vong lap 
for i in range(40):
    turtle.seth(-dotre)
    turtle.color(col[ind]) # Lấy màu từ vị trí ind trong danh sách col và đặt nó làm màu vẽ hiện tại của rùa.
    if  ind == 10 : #Kiểm tra xem giá trị của ind có bằng 11 (vượt quá giới hạn của danh sách col) hay không.
                     #ind = 0: Nếu đúng, đặt lại ind về 0 để bắt đầu lại từ đầu danh sách màu.
        ind = 0
    else:
        ind += 1
    draw(100)
    dotre += 10 #mỗi hinh sẽ lệch đi 1 đơn vị = dotre
t.done()

  
  
 

 

 

