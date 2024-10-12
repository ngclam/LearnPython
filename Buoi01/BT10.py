def ptBac1(a,b ):
    if a == 0:
        if b == 0:
            return "vô số nghiệm"
        else:
            return "vô nghiệm"
    else:
        x= -b/a
        return x         #-b/a    

try:
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    giaiPt = ptBac1(a,b)

    print(f"Phương trình có nghiệm = {giaiPt}")
except ValueError:
    print("Chỉ được nhập số!!!")
