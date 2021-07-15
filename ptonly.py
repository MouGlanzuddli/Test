<<<<<<< HEAD
import math
#Tính pt nhưng đc viết bởi 1 kon newpie ngunguk
def phuong_trinh(a, b):
    if a == 0:
        if b == 0:
            print("Pt có vô số nghiệm")
        if b != 0:
            print("Pt vô nghiệm")
    else:
        print("Pt có một nghiệm duy nhất là: ", -b / a)
print("Pt bậc nhất ax + b = 0")
x = float(input("Nhập giá tri x: "))
y = float(input("Nhập giá tri y: "))
phuong_trinh(x, y)


def pt_2_an(a, b, c):
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ", + (-c / b))
        return
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b ** 2 + delta) / 2 * a
            x2 = (-b ** 2 - delta) / 2 * a
            print("Pt có 2 nghiệm pb x1 =", x1 ,"x2 =", x2)
        elif delta == 0:
            x = -b / (2 * a)
            print("Pt có nghiệm kép x1=x2= ", x)
        else:
            print('Pt vô nghiệm')
print("Pt bậc 2 ax^2 + bx + c")
x = float(input("Nhập tham số 1: "))
y = float(input("Nhập tham số 2: "))
z = float(input("Nhập tham số tự do: "))
pt_2_an(x, y ,z)
=======
import math
#Tính pt nhưng đc viết bởi 1 kon newpie ngunguk
def phuong_trinh(a, b):
    if a == 0:
        if b == 0:
            print("Pt có vô số nghiệm")
        if b != 0:
            print("Pt vô nghiệm")
    else:
        print("Pt có một nghiệm duy nhất là: ", -b / a)
print("Pt bậc nhất ax + b = 0")
x = float(input("Nhập giá tri x: "))
y = float(input("Nhập giá tri y: "))
phuong_trinh(x, y)


def pt_2_an(a, b, c):
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ", + (-c / b))
        return
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b ** 2 + delta) / 2 * a
            x2 = (-b ** 2 - delta) / 2 * a
            print("Pt có 2 nghiệm pb x1 =", x1 ,"x2 =", x2)
        elif delta == 0:
            x = -b / (2 * a)
            print("Pt có nghiệm kép x1=x2= ", x)
        else:
            print('Pt vô nghiệm')
print("Pt bậc 2 ax^2 + bx + c")
x = float(input("Nhập tham số 1: "))
y = float(input("Nhập tham số 2: "))
z = float(input("Nhập tham số tự do: "))
pt_2_an(x, y ,z)
>>>>>>> 137c05d5d44d2356f9002d9b8634d1bfdaeee71b
