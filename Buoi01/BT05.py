def xuatSoNhoNhat(a, b, c, d):
    if a < b and a < c and a < d:
        return a
    elif b < a and b < c and b < d:
        return b
    elif c < a and c < b and c < d:
        return c
    else:
        return d
    
# def xuatSoNhoNhat(a, b, c, d):
#     minNum = min(a, b, c, d)
#     return minNum
    
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

soNhoNhat = xuatSoNhoNhat(a, b, c, d)

print(f"Số nhỏ nhất trong 4 số là: {soNhoNhat}")
   