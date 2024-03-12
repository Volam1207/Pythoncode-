
tienchi = int(input("Bạn đã chi bao nhiêu tiền tại cửa hàng? "))


if tienchi < 75:
    
    tongtienchi = tienchi
elif tienchi >= 75 and tienchi < 100:
    
    tongtienchi = tienchi - 15
elif tienchi >= 100 and tienchi < 150:
     
    tongtienchi = tienchi - 25
else:
    
    tongtienchi = tienchi - 50


print("Tổng số tiền phải thanh toán là:", tongtienchi)