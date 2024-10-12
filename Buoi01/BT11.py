import math
def PTBac2(a,b,c):
    if (a==0):
        if (b==0 and c==0):
            return "phương trình bậc 1 vô số nghiệm !"
        elif (b==0 and c!=0):
            return "phương trình bậc 1 vô nghiệm !"
        else:
            x = -c/b
            return f"phương trình bậc 1 có nghiệm x = {x}"
    else:
        delta = (b**2) - (4*a*c)
        if (delta<0):
            return "phương trình bậc 2 vô nghiệm !"
        elif (delta==0):
            x = -b/(2*a)
            return f"phương trình bậc 2 có nghiệm kép x= {x}"
        else:
            x1 = (float)(-b - math.sqrt(delta)) / (2 * a)
            x2 = (float)(-b + math.sqrt(delta)) / (2 * a)
            return f"phương trình bậc 2 có 2 nghiệm phân biệt: x1= {x1} , x2= {x2} "     
          
try:
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    GiaiPTBac2 = PTBac2(a,b,c)
    print(GiaiPTBac2)

except ValueError:
    print("Vui lòng nhập số !!!")


