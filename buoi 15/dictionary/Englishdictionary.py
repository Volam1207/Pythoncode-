tu_dien ={
     "Hello" : "Xin chào",
    "Bye" : "Tạm biệt",
    "Morning":"Buổi sáng ",
    "Evening" : "Buổi tối",
    "Computer" : "Máy tính",
    "dictionary" : "Từ điển"
}

Tucantra = input("Nhap vao tu can tra: ")
if Tucantra in tu_dien:
    #dùng hàm f " "
    print(f"{Tucantra} co ý nghĩa là {tu_dien[Tucantra]}")
else:
    print(f"{Tucantra} không có trong từ điển")
