#Viết chương trình đếm số lần xuất hiện của một từ trong một văn bản nhất định (đã cho sẵn)
def count_num(n):

  num_words = {} #{} khai báo từ điển rỗng 
  ds = n.split() #{}
  for word in ds:
    word = word.lower().strip()
    app = num_words.get(word, 0)
    num_words[word] = app + 1
  return num_words

nhap = input("Nhập văn bản: ")
app = count_num(nhap)
for word, count in app.items(): #.item phương thức được sử dụng để lấy ra các cặp key-value trong dictionary dưới dạng tuple.
  print(word,count)
  #print(f"{word}: {count}")

