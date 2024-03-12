import math
#nhap du lieu 
a = float(input("Nhap so a : "))
b = float(input("Nhap so b : "))
c = float(input("Nhap so c : "))
#tinh dien tich 
cv = (a+b+c)/2
s = math.sqrt(cv*(cv-a)*(cv-b)*(cv-c))
#in ket qua 
print (s)
