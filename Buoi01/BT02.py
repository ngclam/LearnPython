import math
def tinhDienTich(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a + b > c and a + c > b and b + c > a: 	# Dieu kien de thanh tam giac
        dienTich = tinhDienTich(a, b, c)
        print(f"Diện tích tam giác là: {dienTich}")
    else:
        print("Ba cạnh a, b, c không tạo thành một tam giác hợp lệ")
except ValueError:
    print("Chỉ được nhập số!!!")