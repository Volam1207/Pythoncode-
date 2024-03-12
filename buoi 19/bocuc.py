#inport tkinter
from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry("400x250")
#doi mau nen
root.config(bg = "green")
#than bai
#x và y là tọa độ
Label(root,text = "Name"). place(x = 30, y =50)
Label(root,text = "Email").place(x=30, y= 90)
Label(root,text = "Password").place(x=30, y=130)

Entry(root).place(x = 80, y = 50)
Entry(root).place(x = 80, y = 80)
Entry(root).place(x = 95, y = 130)

root.mainloop()
