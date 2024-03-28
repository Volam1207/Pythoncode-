# Khai báo danh sách sản phẩm
prods_db = {}

def get_product_info(prods_db, prod_id):

  if prod_id in prods_db:
    return prods_db[prod_id]
  else:
    return None

def update_product_info(prods_db, prod_id, new_name):
  """
  Cập nhật tên sản phẩm dựa vào id

  Args:
    prods_db: Danh sách sản phẩm
    prod_id: Id sản phẩm cần cập nhật
    new_name: Tên mới của sản phẩm
  """
  prods_db[prod_id] = {"name": new_name}

# In danh sách sản phẩm hiện tại
print("Danh sách sản phẩm hiện tại:")
for prod_id, prod_info in prods_db.items():
  print(f"- Id: {prod_id}, Tên: {prod_info['name']}")

# Khởi tạo vòng lặp
while True:
  # In các lựa chọn
  print("\nChọn chức năng bạn muốn thực hiện:")
  print("1. Thêm sản phẩm mới")
  print("2. Cập nhật tên sản phẩm")
  print("3. Xóa sản phẩm")
  print("4. Thoát khỏi ứng dụng")

  # Lấy lựa chọn của người dùng
  option = int(input())

  # Xử lý lựa chọn
  if option == 1:
    # Thêm sản phẩm mới
    product_id = int(input("Nhập id sản phẩm mới: "))
    product_info = get_product_info(prods_db, product_id)
    if product_info is not None:
      print(f"Sản phẩm với id {product_id} đã tồn tại.")
    else:
      product_name = input("Nhập tên sản phẩm mới: ")
      update_product_info(prods_db, product_id, product_name)
      print("Thêm sản phẩm thành công.")

  elif option == 2:
    # Cập nhật tên sản phẩm
    product_id = int(input("Nhập id sản phẩm cần cập nhật: "))
    product_info = get_product_info(prods_db, product_id)
    if product_info is not None:
      product_name = input("Nhập tên mới cho sản phẩm: ")
      update_product_info(prods_db, product_id, product_name)
      print("Cập nhật sản phẩm thành công.")
    else:
      print(f"Sản phẩm với id {product_id} không tồn tại.")

  elif option == 3:
    # Xóa sản phẩm
    product_id = int(input("Nhập id sản phẩm cần xóa: "))
    product_info = get_product_info(prods_db, product_id)
    if product_info is not None:
      del prods_db[product_id]
      print("Xóa sản phẩm thành công.")
    else:
      print(f"Sản phẩm với id {product_id} không tồn tại.")

  elif option == 4:
    # Thoát khỏi ứng dụng
    break

  else:
    # Lựa chọn không hợp lệ
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

# In danh sách sản phẩm sau khi quản lý
print("\nDanh sách sản phẩm sau khi quản lý:")
for prod_id, prod_info in prods_db.items():
  print(f"- Id: {prod_id}, Tên: {prod_info['name']}")