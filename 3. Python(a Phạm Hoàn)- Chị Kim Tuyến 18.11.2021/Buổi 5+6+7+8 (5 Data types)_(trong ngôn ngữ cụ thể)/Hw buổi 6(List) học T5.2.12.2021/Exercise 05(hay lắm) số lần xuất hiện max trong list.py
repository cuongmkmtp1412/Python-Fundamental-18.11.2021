'''
Bài 05. Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
'''
n = int(input('Enter the number of elements of list = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

#help(list.count)   
#https://www.howkteam.vn/q/bai-tap-python-ve-hien-phan-tu-xuat-hien-nhieu-nhat-41650
# Coi mỗi phần tử-kể cả các phần tử giống nhau là một phần tử riêng biệt. 
b = []      # Số lần xuất hiện của mỗi phần tử lần lượt là. 
c = []      # Các phần tử có cùng số lần xuất hiện và cao nhất
for i in range(len(inputed_list)-1): 
    b.append(inputed_list.count(inputed_list[i]))

for i in range(len(b)-1):
    if b[i] == max(b):
        c.append(inputed_list[i])

print(f'Một trong các phần tử có số lần xuất hiện nhiều nhất là: {c[0]}')
### Bài hay lắm
# Khó hơn một chút thì: Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
        # thì cũng phải in hết ra. 