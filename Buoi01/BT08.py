def ktNam(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
    
try:
    nam = int(input("Nhập vào một năm: "))

    
    if ktNam(nam):
        print(f"Năm {nam} là năm nhuận.")
    else:
        print(f"Năm {nam} không phải là năm nhuận.")
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")