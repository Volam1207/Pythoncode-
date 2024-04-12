class student : 
    #khai bao ham luu tru danh sach
    danh_sach = []
    #xem danh sach 
    def xemds(self):
        for sv in self.danh_sach:
            print("===== Danh Sach Sinh vien =====\n Sinh Vien: ",sv )
    #them sinh vien 
    def themsv(self,sv):
        self.danh_sach.append(sv)
    #capnhat
    def capnhat(self,vitri,giatri):
        self.danh_sach[vitri] = giatri  
    #xoa sinh vien 
    def xoa(self, vitri):
        del self.danh_sach[vitri]
    #timsv
    def timkiem(self, vitri):
        return self.danh_sach[int(vitri)]
    #sapxep
    def sapxep(self):
        self.danh_sach.sort()
  


#SV.themsv("Tran Tuan Hung")
#SV.themsv("Tran Trong Lam")
#SV.xemds() 
#print("=====Sau khi cap nhat====")
#SV.capnhat(0,"Vo Le Thao My")
#SV.capnhat(1,"Vo Tuan Hung")
#SV.xemds() 
#SV.sapxep
while True:
    SV = student()
    print("=====================================")
    ask = input("Nhập lựa chọn của bạn: \n1 Xem danh sach \n2 Thêm sinh viên \n3 Cập nhật danh sách \n4 Xóa \n5 Sắp Xếp \n6 Tìm kiếm \n7  Thoát: ")
    print("=====================================")
    if ask == "1":
        SV.xemds()
    elif ask == "2":
       Sl = int(input("============= \nNhập số lượng sinh viên cần thêm: "))
       for i in range(Sl):
            ten = input(f"Nhập tên sinh viên {i + 1}: ")
            SV.themsv(ten)
    elif ask == "3":
        vitri = int(input("Nhập vị trí hiện tại: "))
        giatri = input("Nhập giá trị cần cập nhật: ")
        SV.capnhat(vitri, giatri)
    elif ask == "4":
        vitri ="============= \nNhap vị trí cần xóa: "
        SV.xoa(vitri)
    elif ask == "5":
        SV.sapxep()
    elif ask == "6":
       vitri = int(input("============= \nNhập vị trí cần tìm: "))
       vt = vitri - 1
       print("Sinh vien ban dang tim la: ", SV.timkiem(vt))
    elif ask == "7":
        break
    else:
        print("============= \nNhập sai! Nhập lại: ")



