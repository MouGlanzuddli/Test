import math
#1. In toàn bộ số chẵn từ 1000 đến 2000
i = 1000
for i in range(1000, 2001):
    if i % 2 != 0: pass
    else:
        print(i)


#2. Viết chương trình, cho phép người dùng nhập vào một dãy số cách nhau bằng dấu phẩy.
# In ra tổng của các số đã nhập.

number = (input("Nhap day sooo: "))
kq = number.split(',')
try:
    a = map(int, kq)
    sum = sum(a)
    print(sum)
except:
    print("Khong hop le")
    pass

#3.Viết chương trình, cho người dùng nhập vào một xâu.
# In ra xâu đã nhập với tất cả các ký tự được viết hoa


word = str(input("Nhap ki tu: "))
print(word.upper())

#4.Viết chương trình, cho người dùng nhập vào một dãy số cách nhau bằng khoảng trắng.
# In ra danh sách chứa các số đó theo thứ tự tăng dần với các phần tử trùng lặp bị loại bỏ.

def kiemtra(dayso):
    kq = ""
    for trung in dayso:
        if dayso not in kq:
            kq += dayso
    return kq


a = input("Nhap day so: ")
print(kq)

