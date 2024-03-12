# Khởi tạo list
listso = [-2, -1, 0, 1, 2, 3]
# Tìm số lớn nhất
solonnhat = max(listso)
# Xác định vị trí của số lớn nhất
vitri = listso.index(solonnhat)

# Xóa số lớn nhất khỏi list
listso.pop(vitri)
# Tìm số lớn thứ hai
solonnhi = max(listso)
# In kết quả
print("so lon nhat la: ", solonnhat)
print("so lon hai la: ", solonnhi)