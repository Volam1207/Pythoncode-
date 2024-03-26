import time
from datetime import datetime

# Lấy thời gian hiện tại
now = datetime.now()

# Định dạng thời gian
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")

# Vẽ mặt đồng hồ
print("-" * 20)
print("  {}:{}:{}".format(hour, minute, second))
print("-" * 20)

# Chờ 1 giây
time.sleep(1)

# Lặp lại để cập nhật thời gian liên tục
while True:
    # Lấy thời gian hiện tại
    now = datetime.now()

    # Định dạng thời gian
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    # Xóa màn hình
    print("\033[H\033[J")

    # Vẽ mặt đồng hồ
    print("-" * 20)
    print("  {}:{}:{}".format(hour, minute, second))
    print("-" * 20)

    # Chờ 1 giây
    time.sleep(1)