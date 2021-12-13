# Đoàn Ngọc Cường _ 6.12.2021
'''
Bài 03. Viết chương trình tạo ra list mới
bằng cách ghép một chuỗi s vào các phần tử list cũ.
'''
n = int(input('Enter the number of elements of list = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

s = input('Enter string s: ')

new_list = []
for i in inputed_list:
    new_list.append(i + s) 
print(f'Ghép một chuỗi s vào các phần tử list cũ ta được: {new_list}')
