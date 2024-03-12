number = int(input("nhap so (tu 1 den 7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[number - 1] if 1 <= number <= 7 else "so nhap vao sai ")