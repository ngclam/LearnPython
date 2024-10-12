def ktNamNhuan(Nam):
    return (Nam % 4 == 0 and Nam % 100 != 0) or (Nam % 400 == 0)

def tinhNgayTrongThang(Nam, Thang):
    # Xác định số ngày trong tháng
    if Thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif Thang in [4, 6, 9, 11]:
        return 30
    elif Thang == 2:
        return 29 if ktNamNhuan(Nam) else 28
    else:
        return None  # Trả về None nếu tháng không hợp lệ

# Nhập năm và tháng từ người dùng
Nam = int(input("Nhập Năm (ví dụ: 1992, 2008): "))
Thang = int(input("Nhập Tháng (1-12): "))

# Tính số ngày trong tháng
Ngay = tinhNgayTrongThang(Nam, Thang)

if Ngay is not None:
    print(f"Năm {Nam} Tháng {Thang} có {Ngay} Ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập Tháng từ 1 đến 12.")