from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("450x450")
root.title("Máy tính")

#====== THÂN CHƯƠNG TRÌNH

#====== THÂN CHƯƠNG TRÌNH

# Tạo ô input
nhapso = Entry(root,width=50) #khoi tao doi tuong nhap so tu lop Entry
nhapso.grid(row=0,columnspan=4,pady=10,padx=50) #goi den phuong thuc grid

# Hàm xử lý khi nhấn vào các phím 0,1,2,3,4,5,6,7,8,9,+,-,*,/, dấu chấm
def onEqual():
    #lay gia tri trong o input
    value = nhapso.get()
    # Xu ly bieu thuc
    result = eval(value)
    # xoa du lieu trong o va dua vao noi dung moi
    nhapso.delete(0, 'end')
    nhapso.insert('end',result)

def onClear():
    # Xoa toan bo ô input
    nhapso.delete(0, 'end')

def onPress(number):
    # Thêm dữ liệu vào phía sau ô input
    nhapso.insert('end',number)
# Tạo các phím bấm
Button( root,width=4,height=2, text="1", command=lambda:onPress('1') ).grid( row=1,column=0,pady=2 )
#pady = 2  Thêm khoảng đệm 2 pixel xung quanh nút trên trục dọc (y). Điều này tạo ra một khoảng cách giữa nút và các nút lân cận trong lưới.
#lambda khi button nhấn vào mới xử lý 
Button(root,width=4,height=2, text="2", command=lambda: onPress('2')).grid( row=1,column=1 )
Button(root,width=4,height=2, text="3", command=lambda: onPress('3')).grid( row=1,column=2 )
Button(root,width=4,height=2, text="+", command=lambda: onPress('+')).grid( row=1,column=3 )

Button(root,width=4,height=2, text="4", command=lambda: onPress('4')).grid( row=2,column=0 )
Button(root,width=4,height=2, text="5", command=lambda: onPress('5')).grid( row=2,column=1 )
Button(root,width=4,height=2, text="5", command= lambda: onPress('5')).grid( row=2,column=2 )
#
Button(root,width=4,height=2, text="-", command=lambda: onPress('-')).grid( row=2,column=3 )

Button(root,width=4,height=2, text="7", command=lambda: onPress('7')).grid( row=3,column=0 )
Button(root,width=4,height=2, text="8", command=lambda: onPress('8')).grid( row=3,column=1 )
Button(root,width=4,height=2, text="9", command=lambda: onPress('9')).grid( row=3,column=2 )
Button(root,width=4,height=2, text="*", command=lambda: onPress('*')).grid( row=3,column=3 )

Button(root,width=4,height=2, text="0", command=lambda: onPress('0')).grid( row=4,column=0 )
Button(root,width=4,height=2, text="/",command=lambda: onPress('/')).grid( row=4,column=3 )
Button(root,width=4,height=2, text="Clear", command=onClear).grid( row=4,column=2 )
Button(root,width=4,height=2, text="=", command=onEqual).grid( row=4,column=1 )

Button(root,width=4,height=2, text=".").grid( row=5,column=0 )

#====== KẾT THÚC PHẦN THÂN

#====== KẾT THÚC PHẦN THÂN


root.mainloop()
