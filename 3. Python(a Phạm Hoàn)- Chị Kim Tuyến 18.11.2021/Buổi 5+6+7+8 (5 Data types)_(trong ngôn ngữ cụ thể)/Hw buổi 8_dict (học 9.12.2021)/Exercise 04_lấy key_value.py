# Đoàn Ngọc Cường: 13.12.2021
'''
Bài 04. Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
'''
my_dict1 = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'1': 'a', '2': 'b', '3': 'c'}
# my_dict = my_dict1 + my_dict2  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print('Các key-value trong my_dict1 là: ', end = '')
for key1 in my_dict1: 
    print(f'{key1}: {my_dict1[key1]}', end = ',')
print()

print('Các key-value trong my_dict2 là: ', end = '')
for key2 in my_dict2: 
    print(f'{key2}: {my_dict2[key2]}', end =',')   
    # # Khi mình quên và để my_dict1[key2], thì gặp lỗi: KeyError: '1'
print()
