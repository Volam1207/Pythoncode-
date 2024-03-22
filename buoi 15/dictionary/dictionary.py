tu_dien = {
    "ten" : "Nguyễn Thế Võ Lâm",
    "tuoi" : 22,
    "cam_nang" : 72
}
#lap phan tu trong tu dien
print(tu_dien["ten"])
#cach lay 
print(tu_dien.get("tuoi"))
#update
tu_dien.update({"so thich" : "da bong"})
print(tu_dien.get("so thich"))
#thay doi can nang
tu_dien['can nang']='75'
#xoa can nang 
tu_dien.pop('can nang')
#xoa tu dien 
tu_dien.clear()