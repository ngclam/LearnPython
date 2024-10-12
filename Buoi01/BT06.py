def xuatSoNhoNhat(a, b, c, d):
    minNum = min(a, b, c, d)
    return minNum
    
def xuatSoLonNhat(a, b, c, d):
    maxNum = max(a, b, c, d)
    return maxNum

a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số nguyên b: "))
c = float(input("Nhập số nguyên c: "))
d = float(input("Nhập số nguyên d: "))

soNhoNhat = xuatSoNhoNhat(a, b, c, d)
soLonNhat = xuatSoLonNhat(a, b, c, d)
print(f"Số nhỏ nhất trong 4 số là: {soNhoNhat}" )
print(f"Số lớn nhất trong 4 số là: {soLonNhat}" )