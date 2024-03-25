list = [20,45,6,8,10,25,41]
 # Nhập chuỗi số từ bàn phím
#chuoi_so = input("Nhập chuỗi số: ")
# Chuyển đổi chuỗi số thành danh sách các số nguyên
#danh_sach_so = list(map(int, chuoi_so.split()))
def getmin(list):
    min = list[0]
    for i in list :
        if i <  min :
            min = i
    return min
print ("Giá trị nhỏ nhất trong", list , " là : ", getmin(list))
def getmax(list):
    min = list[0]
    for i in list :
        if i >  max :
            max = i
    return max 
print ("Giá trị lớn nhất trong", list , " là : ", getmax(list))