import random

# Hàm tạo số ngẫu nhiên
def tao_so_ngau_nhien():
  return random.randint(0, 9)

# Hàm so sánh số đoán và số ngẫu nhiên
def so_sanh(M, so_ngau_nhien):
  if M == so_ngau_nhien:
    return True
  else:
    return False

# Hàm chơi game
def choi_game():
  # Tạo số ngẫu nhiên
  N = tao_so_ngau_nhien()

  # Lặp lại cho đến khi người dùng đoán đúng
  while True:
    # Nhập số đoán từ người dùng
    M = float(input("Nhập số bạn đoán: "))

    # So sánh số đoán và số ngẫu nhiên
    if so_sanh(M, N):
      print("Chúc mừng bạn đã đoán đúng!")
      break
    else:
      print("Số bạn đoán không chính xác. Hãy thử lại!")

# Chơi game
choi_game()