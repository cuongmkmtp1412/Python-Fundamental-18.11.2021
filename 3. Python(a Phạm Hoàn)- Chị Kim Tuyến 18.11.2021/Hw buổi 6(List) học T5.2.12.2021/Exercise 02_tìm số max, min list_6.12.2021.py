# Đoàn Ngọc Cường 6.12.2021

'''
Bài 02. Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
'''

n = int(input('Enter the number of elements of list = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

number_inputed_list = []
for i in inputed_list:
    try: #if  '0' <= i <= '9': # ValueError: could not convert string to float: '2fsf'
        i = float(i)
        number_inputed_list.append(i)   # Ban đầu nhầm: i.append(number_inputed_list)
    except: 
        continue
print(f'Số lớn nhất trong list là: {max(number_inputed_list)}')
print(f'Số nhỏ nhất trong list là: {min(number_inputed_list)}')