print("+--------------MENU-----------------+")
print("|Chon C de tao hoa don              |")
print("|Chon R de xem thong tin hoa don    |")
print("|Chon T de tinh tong doanh thu      |")
print("|Chon A de tinh tong hang hoa ban ra|")
print("|Chon E de thoat                    |")
print("+-----------------------------------+")

# danhsachhoadon=[]
danhsachhoadon = [
    {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS01', 'tongtientruocthue': 25000},
    {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS02', 'tongtientruocthue': 25000}
]

while True:
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'C':
        print("moi ban tao hoa don")
        hoadon={}
        hoadon["sohoadon"] = input("nhap so hoa don:")
        hoadon["ngayhoadon"]= input("nhap ngay hoa don :")
        hoadon["nguoimua"]= input("nhap nguoi mua hang :")
        hoadon["tongtientruocthue"] = 0
        hoadon["thue"] = 0.1
        hoadon["tongtien"] = 0
        hoadon["danhsachhanghoa"] = []

        nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
        while nhaphanghoa.upper() == 'Y':
            hanghoa = {}
            hanghoa["stt"] = input("nhap so thu tu: ")
            hanghoa["ten"] = input("nhap ten hang hoa: ")
            soluong = input("nhap so luong: ")
            hanghoa["soluong"] = int(soluong)
            hanghoa["dongia"] = int(input("nhap don gia:"))
            hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
            hoadon["danhsachhanghoa"].append(hanghoa)

            hoadon["tongtientruocthue"] = hoadon["tongtientruocthue"] + hanghoa["thanhtien"]

            nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")

        hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"]*hoadon["thue"]
        danhsachhoadon.append(hoadon)
        print("Kiemtra:", danhsachhoadon)

    if x.upper() == 'R':
        timthay = False
        while timthay is False:
            sohoadon_canxem = input("nhap so hoa don can xem:")
            for hoadon in danhsachhoadon:
                if hoadon["sohoadon"] == sohoadon_canxem:
                    timthay = True
                    #Hoa don se in o day
                    print("                          HOA DON MUA HANG                                  ")
                    print("so hoa don:",hoadon["sohoadon"])
                    print("ngay xuat:",hoadon["ngayhoadon"])
                    print("ten khach hang:",hoadon["nguoimua"])
                    print("_____________________________thong tin hoa don_______________________________")
                    print("+----------+------------------+----------+---------------+------------------+")
                    print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
                    print("+----------+------------------+----------+---------------+------------------+")

                    for hanghoa in hoadon["danhsachhanghoa"]:
                        print("In dong hang hoa o day")
                        #print("| "+stt_x+"  | " +tenhanghoa+ " | "+soluong_x+" | "+dongia_x+" | "+thanhtien_x+" |")
                    print("+----------+------------------+----------+---------------+------------------+")
                    #end of Hoa don se in o day
                    break
    if x.upper() == 'T':
        tongdoanhthu = 0
        for hoadon in danhsachhoadon:
            tongdoanhthu = tongdoanhthu + hoadon["tongtien"]
        print("Tong doanh thu la: ", tongdoanhthu)

    if x.upper() == 'A':
        tongsohanghoa = 0
        doanhsoban = 0

        tenhanghoa = input("nhap ten hang hoa can xem:")
        for hoadon in danhsachhoadon:
            for hanghoa in hoadon["danhsachhanghoa"]:
                if hanghoa["ten"] == tenhanghoa:
                    tongsohanghoa = tongsohanghoa + hanghoa["soluong"]
                    doanhsoban = doanhsoban + hanghoa["thanhtien"]
                    break
        print("Tong so hang hoa: ", tongsohanghoa)
        print("Doanh so ban: ", doanhsoban)

    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break

