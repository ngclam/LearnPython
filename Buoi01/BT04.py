def xuatSoNhoNhat(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

soNhoNhat = xuatSoNhoNhat(a, b, c)

print(f"Số nhỏ nhất trong 3 số là: {soNhoNhat}")
   