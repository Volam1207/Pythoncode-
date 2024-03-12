kitu = input('nhap ki tu ban chon: ')
cao = int(input('nhap chieu cao: '))
rong = int(input('nhap chieu rong: '))
for i in range(1, cao + 1):
    print_str = ''
    for j in range(1, rong + 1):
        if i == 1 or i == cao: #Nếu là hàng đầu tiên hoặc hàng cuối cùng thì chuỗi in sẽ được cộng thêm ký tự in
            print_str += kitu
           
        else:
            if j == 1 or j == rong: 
                 print_str += kitu 
            #Nếu không thì chuỗi in sẽ được cộng ký tự ở những vị trí 
            #thuộc cạnh bên trái và cạnh bên phải hình, những vị trí còn lại sẽ được cộng với ký tự space
            else:
                print_str += ' ' #neu khong trung dau hoac cuoi thì sẽ in ra dấu trống (space)
    print(print_str)
            