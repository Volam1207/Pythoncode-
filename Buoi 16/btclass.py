class HCN: 
    cd = 0 
    cr = 0 
    def dientich(self):
        dientichcuan = self.cd *self.cr 
        return dientichcuan
    def tinhchuvi(self):
        return 2 * (self.cd+self.cr)
#khoi tao doi tuong hcn 1
hcn_1 = HCN() 
hcn_1.cd = 4
hcn_1.cr = 5
#tinhdt 
dt = hcn_1.dientich()
#tinhcv
cv = hcn_1.tinhchuvi()
print("Dien tich hcn la: ",dt)
print("chu vi hcn la: ",cv)
