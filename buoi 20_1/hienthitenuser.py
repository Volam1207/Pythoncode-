from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Họ và Tên")
#khai bao ham xu ly nhap
def hovaten(): #đătt tên trong str phải trùng tên hàm 
    num1 = str(ho.get())
    num2 = str(ten.get())
    result = num1 + " " + num2
    kq.config(text="Xin chao" + " " + str(result))
Label(root, text = "Họ").grid(row = 0, column = 0)
#capnhat o input1
ho = Entry(root)
ho.grid(row = 0, column = 1)
Label(root, text = "Tên").grid(row = 1, column = 0)
#capnhat o input 2
ten = Entry(root)
ten.grid(row = 1, column = 1)
Button(root, text = "Xử Lý ",command = hovaten).grid(row = 2, column = 0)
#capnhat label kq
kq=Label(root,text="Xin chao")
kq.grid(row = 2, column = 1)
root.mainloop()
