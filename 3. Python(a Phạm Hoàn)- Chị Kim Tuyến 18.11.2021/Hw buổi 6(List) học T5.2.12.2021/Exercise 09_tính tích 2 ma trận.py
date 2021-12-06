#Đoàn Ngọc Cường
'''
Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 
(Gợi ý: dùng list chứa list).
'''
# Nhập ma trận vuông cấp 3: 
'''
https://quantrimang.com/ma-tran-trong-python-160014
Ma trận trong Python sử dụng nested list and thư viện NumPy.
'''
import numpy as np

# Nhập matrix A
support_A = []              
for i in range(0, 3*3): 
    _input = input("Nhập matrix A từ phải sang trái, từ trên xuống dưới: ")          
    support_A.append(_input)
A = []
A.extend( [ support_A[0:3], support_A[3:6], support_A[6:9] ] )
print(A)
A = np.array(A)

# Nhập matrix B
support_B = []              
for i in range(0, 2*2): 
    _input = input("Nhập matrix B từ phải sang trái, từ trên xuống dưới: ")          
    support_B.append(_input)
B = []
B.extend( [ support_A[0:3], support_A[3:6], support_A[6:9] ] )
print(B)
B = np.array(B)

#A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C = A.dot(B)      
print(C)

