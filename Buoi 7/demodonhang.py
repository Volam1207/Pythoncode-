# Hỏi người dùng đã chi bao nhiêu tiền
tienchi = int(input("Bạn đã chi bao nhiêu tiền tại cửa hàng? "))

# Tính tổng số tiền phải thanh toán
tongthanhtoan = tienchi if tienchi < 75 else tienchi - 15 if tienchi >= 75 and tienchi < 100 else tienchi - 25 if tienchi >= 100 and tienchi < 150 else tienchi - 50

# In ra tổng số tiền phải thanh toán
print("Tổng số tiền phải thanh toán là:", tongthanhtoan)