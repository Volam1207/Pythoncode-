import math
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("conver")

#ham xu ly do F 
def converF():
    F = float(doF.get())
    KqC = 5/9 * (F - 32)
    kqC.config(text="Độ C :" + str(KqC))
#tạo label và button cho do F
Label(root, text = "Độ F").grid(row = 0, column = 0)
doF= Entry (root)
doF.grid(row = 0, column = 1)
#label hien thi o do F
Label(root, text = "Do C").grid(row = 0, column = 2)
Button(root, text = "Covert ",command = converF).grid(row = 0, column = 4)
kqF = Label(root, text = " ")
kqF.grid(row = 1, column = 5)


def converC():
    C1 = float(doC.get())
    KqF = (C1 * 1.8) + 32
    kqF.config(text="Độ F :" + str(KqF))
#tao label và button cho do C
Label(root, text = "Độ C").grid(row = 1, column = 0)
doC= Entry (root)
doC.grid(row = 1, column = 1)
#label hien thi o do C
Label(root, text = "Do F").grid(row = 1, column = 2)
Button(root, text = "Covert ",command = converC).grid(row = 1, column = 4)
kqC = Label(root, text = " ")
kqC.grid(row = 0, column = 5)
root.mainloop()