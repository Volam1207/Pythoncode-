from random import *
print("Chào mừng bạn tới với trò chơi")

while True:
    current_number = 0
    current_player = randint(0, 1)
    if current_player == 0 :
        print("Bạn là người bắt đầu")
    else:
        print("Máy tính bắt đầu")
    while current_number <= 21:
        print("Total: ", current_number)
        if current_player == 0:
            player_choice = ""
            while ["1", "2", "3"]  (player_choice) == False:
                print("Input your number:")
                player_choice = input()
                if player_choice != 1 or player_choice != 2 or player_choice != 3 :
                    print("Invalid value, please try again!")   
            print("You: ", player_choice)
            current_number += int(player_choice)
            if current_number >= 21:
                print("You lost!") 
                break
            current_player = 1
        else:
            computer_choice = randint(1,3)
            print("Computer: ", computer_choice)
            current_number += computer_choice
            if current_number >= 21:
                print("You win!") 
                break
            current_player = 0
    print("Do you want to play agian?")
    play_again = input()
    if play_again.__contains__("y") == False:
        break