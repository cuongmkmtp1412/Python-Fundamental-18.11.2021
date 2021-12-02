#Đoàn Ngọc Cường- T2-29/11/2021
'''
Bài 05. Lập chương trình thực hiện các công việc sau:
    1. Nhập số epsilon < 1 từ bàn phím
    2. Tính e = 1 + 1/1! + 1/2! + ... + 1/n! quá trình dừng khi 1/n! < epsilon.
    3. Đưa kết quả ra màn hình
'''
import math 
epsilon = float(input("Nhập số epsilon < 1 = "))
e = 0
n = 0
while 1/math.factorial(n) >= epsilon:
    e += 1/math.factorial(n) 
    n += 1
print(e)            #xấp xỉ = 2.67