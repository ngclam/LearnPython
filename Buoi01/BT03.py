def tinhTong(a,b):
    return a+b
def tinhHieu1(a,b):
    return a-b
def tinhHieu2(a,b):
    return b-a
def tinhTich(a,b):
    return a*b
def tinhThuong(a,b):
    return a/b
def tinhChiaLayDu(a,b):
    return a%b

a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))

print("Tổng (a+b) =", tinhTong(a,b))
print("Hiệu (a-b) =", tinhHieu1(a,b))
print("Hiệu (b-a) =", tinhHieu2(a,b))
print("Tích (a*b) =", tinhTich(a,b))
print("Thương (a/b) =", tinhThuong(a,b))
print("Chia lấy phần dư (a%b) =", tinhChiaLayDu(a,b))