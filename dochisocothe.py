
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Convert")
import math

#ham chuyen doi 
#taolabel cho so kg

def inputkg(kg):
    kg = float(sokg.get())
def convertogr():
    kg1 = float(inputkg.get())
    kqgr = kg1 * 1000
    kqgr.config(text = "Gram: " + str(kqgr))
def convertoO():
    kqounce = inputkg  / 35
    kqounce.config(text = "Gram: " + str(kqounce))
def convertoP():
    kqpound = inputkg  / 2.2
    kqpound.config(text = "Gram: " + str(kqpound))
   
        
#taolabel cho so kg
Label(root,text = "Kilogram").grid(row = 0,column = 0)
#capnhat cho sokg
sokg = Entry (root)
sokg.grid(row =0, column = 1)
#tao button
Button(root, text = "conver", command= convertogr).grid(row = 0, column=3)
#tạo label cho gram 
Label(root,text = "Gram: ").grid(row = 1,column = 1)
#capnhat cho sokg
kq = Entry (root)


#label hien thi quy doi 
#Label(root, text = "Gram").grid(row = 1,column = 1)
#Button(root, text = "conver", command= convertogr).grid(row = 0, column=3)
#kqgr = Label(root, text = " ")
#kqgr.grid(row = 1, column = 0)
root.mainloop()