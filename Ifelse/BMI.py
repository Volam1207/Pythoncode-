import math
h, w = map(float, input("Nhập chiều cao (cm), cân nặng (kg): ").split(","))
BMI =  w / pow(h, 2) #pow là hàm lũy thừa 

if BMI < 16: 
    print("Gầy cấp độ III")
elif 16 <= BMI < 17:
    print("Gầy cấp độ II")
elif 17<= BMI < 18.5: 
    print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
    print("Bình thường")
elif 25 <= BMI < 30: 
    print("Thừa cân")
elif 30 <= BMI < 35 :
    print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
    print("Béo phì cấp độ II")
elif BMI > 40:
    print("Béo phì cấp độ III") 
else:
    print("Nhap không đúng yêu cầu!")


 
 
