print("Nhập số của bạn: ")
player_choice = input() #dùng hàm nhập
               #kiem tra so nhap có đúng khô
if player_choice not in ["1", "2", "3"]:
  # player_choice không hợp lệ
  print("Nhập sai!")
else:
  # player_choice hợp lệ
  print(f"Số bạn nhập: {player_choice}")