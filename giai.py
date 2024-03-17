
from tkinter import *
from tkinter import ttk
import tkinter as tk
root = Tk()
#window = tk.Tk()
#window.title("Chuyển đổi đơn vị cân nặng")

def convert_weight():
  # Lấy giá trị kg
  kg = e2_value.get()

  # Chuyển đổi sang gram
  gram = float(kg) * 1000

  # Chuyển đổi sang pound
  pound = float(kg) * 2.20462

  # Chuyển đổi sang ounce
  ounce = float(kg) * 35.274

  # Cập nhật giá trị gram
  e3.delete("1.0", END)
  e3.insert(END, gram)

  # Cập nhật giá trị pound
  e4.delete("1.0", END)
  e4.insert(END, pound)

  # Cập nhật giá trị ounce
  e5.delete("1.0", END)
  e5.insert(END, ounce)
  # Nhãn nhập kg
e1 = tk.Label(text="Nhập kg:")
e1.grid(row=0, column=0)

# Biến lưu trữ giá trị kg
e2_value = tk.StringVar()

# Trường nhập kg
e2 = tk.Entry(textvariable=e2_value)
e2.grid(row=0, column=1)

# Nút chuyển đổi
b1 = tk.Button(text="Chuyển đổi", command=convert_weight)
b1.grid(row=0, column=2)

# Nhãn Gram
e3 = tk.Label(text="Gram:")
e3.grid(row=1, column=0)

# Trường hiển thị giá trị Gram
e3 = tk.Text(height=1, width=20)
e3.grid(row=1, column=1)

# Nhãn Pounds
e4 = tk.Label(text="Pounds:")
e4.grid(row=2, column=0)

# Trường hiển thị giá trị Pounds
e4 = tk.Text(height=1, width=20)
e4.grid(row=2, column=1)

# Nhãn Ounce
e5 = tk.Label(text="Ounce:")
e5.grid(row=3, column=0)

# Trường hiển thị giá trị Ounce
e5 = tk.Text(height=1, width=20)
e5.grid(row=3, column=1)