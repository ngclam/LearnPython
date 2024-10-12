def tinhDienTich(chieuDai, chieuRong):
    return chieuDai * chieuRong

def tinhChuVi(chieuDai, chieuRong):
    return 2 * (chieuDai + chieuRong)

chieuDai = float(input("Nhập chiều dài của hình chữ nhật: "))
chieuRong = float(input("Nhập chiều rộng của hình chữ nhật: "))

dienTich = tinhDienTich(chieuDai, chieuRong)
chuVi = tinhChuVi(chieuDai, chieuRong)

print("Diện tích hình chữ nhật là:", dienTich)
print("Chu vi hình chữ nhật là:", chuVi)