class Date:
    #khai bao thuoc tinh 
    day = 0
    month = 0
    year = 0
    #khai báo phương thức
    def __init__(self,ts_day,ts_month,ts_year) :
        self.day = ts_day
        self.month = ts_month
        self.year = ts_year
    #phương thức trả về thuộc tính 
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getyear(self):
        return self.year
    
    def setday(self,ts_day):
        self.day = ts_day
    def setmonth(self,ts_month):
        self.month = ts_month
    def setyear(self,ts_year):
        self.year = ts_year
    def setDate(self,ts_day,ts_month,ts_year):
        self.day =ts_day
        self.month =ts_month 
        self.year =ts_year 
    def toString(self):
        #str để ép kiểu dl sang dạng chuỗi
        return str(self.day) + '/' + str(self.month) +'/'+ str(self.year)
homnay = Date(24,4,2024)
print (homnay.toString())
#thay doi ngay
homnay.setday(9)
print (homnay.toString())
homnay.setDate(15,6,2024)
print (homnay.toString())
