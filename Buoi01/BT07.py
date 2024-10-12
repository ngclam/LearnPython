def xepLoai(diemTB):
    if diemTB < 0 or diemTB > 10:
        return "Không có điểm này!!!"
    elif diemTB < 5:
        return "Kém"
    elif 5 <= diemTB <= 7:
        return "Trung bình"
    elif 7 < diemTB <= 8:
        return "Khá"
    elif 8 < diemTB <= 9.5:
        return "Giỏi"
    else:
        return "Xuất sắc"
    
try:
    diemTB = float(input("Nhập điểm trung bình: "))
    xepLoai = xepLoai(diemTB)

    print(f"Xếp loại học lực: {xepLoai}")
except ValueError:
    print("Chỉ được nhập số!!!")