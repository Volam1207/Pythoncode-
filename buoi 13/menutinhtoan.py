#vietcachamtinhtoan
def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    return a/b
a = int(input("nhap so thu nhat: "))
b = int(input("nhap so thu hai: "))
choice = input("lựa chọn phép tính(1-4) \n 1-cong \n 2-tru \n 3-nhan \n 4-chia :")

#hàm if để trả về các lựa chọn 
if(choice == "1"):
    print("ket qua là: ",cong(a,b))
elif(choice == "2"):
     print("ket qua là: ",tru(a,b))
elif(choice == "3"):
     print("ket qua là: ",nhan(a,b))
elif(choice == "4"):
     print("ket qua là: ",chia(a,b))
else:
    print("nhap sai gia tri!")
