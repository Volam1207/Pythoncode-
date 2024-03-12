number = int(input("nhap so tu 1 den 7: "))

# Kiểm tra 
if 1 <= number <= 7:
    # In ra ngày tương ứng
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[number - 1])
else:
    print("nhap sai!")