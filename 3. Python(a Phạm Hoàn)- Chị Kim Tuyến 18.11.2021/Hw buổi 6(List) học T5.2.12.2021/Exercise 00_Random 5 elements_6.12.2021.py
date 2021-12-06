# @Đoàn Ngọc Cường 6/12/2021: 2 giờ chiều. 
'''Epsilon Bit  2 thg 12    500 điểm
Bài 00. Viết chương trình sinh list mới bằng cách 
lấy ngẫu nhiên 5 phần tử từ list gốc.
'''

# Cách 1: use random.choice()
'''
#help(choice)
choice(seq) method of random.Random instance. 
Choose a random element from a non-empty sequence.'''
from random import choice

n = int(input('Enter n = '))   # Số phần tử của original_list 
original_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")             #/street 1/
    original_list.append(_input)     #Nhập vào list ban đầu
if len(original_list) < 5:
    print('Original list is not enough 5 elements.')
else: 
    random_list_five_element = []
    while len(random_list_five_element) < 5: 
        x = choice(original_list)
        if x not in random_list_five_element:
            random_list_five_element.append(x)
    print(f'Random 5 elements from list: {random_list_five_element}')

# Cách 2: use numpy.random.choice()
'''# https://vimentor.com/vi/lesson/26-random-mot-so-trong-python 
Hàm choice() của random package thuộc mô đun numpy là thuận tiện hơn,
bởi vì nó cung cấp thêm nhiều options

# py -m pip install numpy (ko có <py -m> thì bị lỗi ???)
Installing collected packages: numpy
Successfully installed numpy-1.21.4
WARNING: You are using pip version 20.1.1; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe -m pip install --upgrade pip' command.

from numpy.random import choice
print(choice(original_list, size=(3,3), replace=False)) 
# replace để tránh bị chọn trùng giữa các bộ 3

'''

#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 596-597: truncated \UXXXXXXXX escape
#Cách giải quyết là avoids the use of escape characters. (https://clay-atlas.com/us/blog/2019/10/27/python-english-tutorial-solved-unicodeescape-error-escape-syntaxerror/), từ \ thành \\ hoặc ...









