# Đoàn Ngọc Cường 13.12.2021
'''
Bài 01. Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất trong các value của dict
'''
# Nhập dict: 
my_dict = {}
while True: 
    key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish>: ")    
    if key == '<finish>':
        break
    else: 
        my_dict[key] = float(input('Enter value float của key mới nhập gần nhất: '))       
print(my_dict)

# my_dict = {'a': 3, 'b': 2, 'c': 3}
max_value = max(my_dict.values())
print(f'Giá trị lớn nhất trong các value của dict đã nhập là: {max_value}')
min_value = min(my_dict.values())
print(f'Và giá trị nhỏ nhất trong các value của dict đã nhập là: {min_value}')

'''
***Cách truy cập và duyệt trong dict***
- dict không có key thì chịu (các kiểu dữ liệu khác thì có index (trừ set ra))
- print(my_dict.get('game')) >>> get return None nếu key không tồn tại, 
còn print (my_dict['name']) sẽ trả lại lỗi
# _item = my_dict.items()    >>> ([('name', 'Một'), (2, [1, 2, 3]), ('age', 2)])  # là type: dict_value not type: List
# _key = my_dict.keys()      >>> (['name', 2, 'age'])
# _value = my_dict.values()  >>> (['Một', [1, 2, 3], 2])

- Duyệt:
# my_dict = {1: 'năm', 2: 3 }
# # Cách 1:
# for k in my_dict: # lấy lần lượt các key ra 
#     print(f'{k}: {my_dict[k]}')
# # Cách 2: sẽ ít dùng vì cách 1 cho nhanh
# for k in my_dict.keys():    # giống y cách 1 vì nó duyệt qua key thôi
#     print(f'{k}: {my_dict[k]}')
# # Cách 3: duyệt qua item 
# for k, v in my_dict.items(): # convert key và value để từng dạng tuple 2 tham số>> ta unpacking nó ra
#     print(f'{k}: {v}')
'''