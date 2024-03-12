def trans(f):
    return(f-32) / 1.8

a = float(input("nhap vo nhieu do can chuyen doi: "))
trans(a)
print("nhiet do can chuyen doi la :", trans(a))