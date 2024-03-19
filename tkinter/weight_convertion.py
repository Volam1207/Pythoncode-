from tkinter import *

root = Tk()
root.geometry("500x600")
root.title("Weight Convert")

def weight_cover():
    kg = e2_value.get() #lấy giá trị từ e2

    gram = float(kg) * 1000
    gram_entry.delete(1.0, END)
    gram_entry.insert(END, gram)

    pounds = float(kg) * 2.20462
    pound_entry.delete(1.0, END)
    pound_entry.insert(END, pounds)

    ounce = float(kg) * 35.274
    ounce_entry.delete(1.0, END)
    ounce_entry.insert(END, ounce)
   
#Khởi tạo GUI
e1 = Label(root, text="Nhập giá trị kg:")  # Sử dụng window làm parent
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
b1 = Button(root, text="Chuyển đổi", command=weight_cover)
e3 = Label(root, text="Gram:")
e4 = Label(root, text="Pound:")
e5 =Label(root, text="Ounce:")

#sắp xếp grid
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
b1.grid(row=0, column=2)
e3.grid(row=1, column=0)
e4.grid(row=2, column=0)
e5.grid(row=3, column=0)
#luu gia trị 
gram_entry = Text(height=1, width=20)
pound_entry = Text(height=1, width=20)
ounce_entry = Text(height=1, width=20)

gram_entry.grid(row=1, column=1)
pound_entry.grid(row=2, column=1)
ounce_entry.grid(row=3, column=1)
root.mainloop()
