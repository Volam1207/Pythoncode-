import random
def taoso():
    return random.randint(0, 9)
N = taoso()

M = float(input("Nhap vao so ban doan: "))
if M == N :
    print("dung")
else:
   print("so may tinh doan la: ", N)
   print ("sai")
    
