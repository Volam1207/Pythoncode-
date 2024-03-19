str = input("nhap chuoi ki tu: ")
#ham tinh chuoi
def count(n):
    kq = 0
    for i in n:
     kq += 1
    return kq
#in ra 
print('Do dai: ', count(str))