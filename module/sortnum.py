num1 = input("Nhap so thu 1: ")
num2 = input("Nhap so thu 2: ")
num3 = input("Nhap so thu 3: ")
if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
print("sau khi sap xep: ", num1, num2,num3)