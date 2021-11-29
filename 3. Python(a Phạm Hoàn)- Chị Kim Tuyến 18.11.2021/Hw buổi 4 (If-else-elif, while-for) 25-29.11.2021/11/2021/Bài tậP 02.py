'''
Bài 02. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím
'''
import math
n = int(input("Enter int n = "))
x= float(input("Enter float x = "))
S_1, S_2, S_3 = 0, 0, 0
for i in range(n+1):
    S_1 += x**i
    S_2 += (-1)**i * x**i
    S_3 += x**i/math.factorial(i)
    # Các hàm có sẵn : https://www.v1study.com/python-tham-khao-cac-ham-toan-hoc-trong-python.html
print(f'S_1 = 1 + x + x^2 + x^3 + ... + x^n = {S_1}')
print(f'S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n = {S_2}')
print(f'S_3 = 1 + x/1! + x^2/2! + ... + x^n/n! = {S_3}')


