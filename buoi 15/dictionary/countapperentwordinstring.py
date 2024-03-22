def dem(n):
    #tao tu dien
    num_word = {}
    text_list = n.split
    for word in text_list():
        word = word.lower().strip() 
        #•	Sử dụng lower() để chuyển các ký tự hoa 
        # sử dụng strip() để loại bỏ các khoản trắng đằng trước hoặc đằng sau 
        app = num_word.get(word, 0)
        num_word[word] = app + 1 #so lan xuat hien + 1 
    return num_word
 
 #tao input 
message = input("Nhap van ban can tao : ")
# Gọi hàm đếm từ và truyền message làm tham số
app = dem(message)
for word,count in app.items():
    print (word,count)
