from random import *
print("chào mừng đến với trò chơi")
List = ["1","2","3"]

#khởi tạo vòng lặp đầu trò chơi
while True:
    #khoi tao bien dem
    current_number = 0
    current_player = randint(0,1)
    if current_player == 0:
        print("Bạn chơi trước")
    else:
        print("Máy tính chơi trước")
    while current_number <= 21:
        #in ra số hiện tại 
        print("Số hiện tại là:",current_number)
        #kiểm tra người chơi hiện tại là người hay máy 
        if current_player == 0:
            player_choice = ""
            while player_choice not in List:
                print("Nhập số của bạn: ")
                player_choice = input() #dùng hàm nhập
               #kiem tra so nhap có đúng không
                if(player_choice not in List): #123 là str không phải số 
                    print("Nhập sai!")
                else: 
                    print("Số bạn nhập: ",player_choice)
            #gan số nhập cho số hiện tại
            current_number += int(player_choice)
            #kiểm tra có lớn hơn hay không
            if current_number >= 21:
                print("Số hiện tại là: ",current_number,"Bạn thua!")
                break
            current_player = 1 #luot choi cua may
        else:
            com_choice = randint(1,3)
            print("Lựa chọn của máy tính: ",com_choice)
            current_number += com_choice
            if current_number >= 21:
                print("Số hiện tại là: ",current_number,"Bạn thắng!")
                break
            current_player = 0

    #chơi lại hay không
    play_again=input('Would you like to play again? ')
    if play_again.lower().startswith("y"):
      continue
    else: 
     print('Bái bai!!!')
     break

  
    
    
       
      

      