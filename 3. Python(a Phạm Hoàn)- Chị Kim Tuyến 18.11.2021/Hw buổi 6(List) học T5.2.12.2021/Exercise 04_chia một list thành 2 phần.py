'''
Bài 04. Viết chương trình chia một list thành 2 phần
 với độ dài phần đầu được nhập vào từ bàn phím.
'''

n = int(input('Enter the number of elements of list = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

n = int(input("Enter độ dài phần đầu muốn chia: "))
list_one = inputed_list[:n]
list_two = inputed_list[n:]
print(list_one)
print(list_two)
