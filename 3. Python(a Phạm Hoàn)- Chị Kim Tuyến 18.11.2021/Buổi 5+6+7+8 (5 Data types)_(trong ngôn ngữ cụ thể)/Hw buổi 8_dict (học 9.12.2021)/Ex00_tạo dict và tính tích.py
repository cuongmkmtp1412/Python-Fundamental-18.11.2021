# Đoàn Ngọc Cường Chiều T2.13.12.2021
'''
Bài 00. Viết chương trình tính tích value của các phần tử trong một dict
'''
# Enter a dict chứa các giá trị float, cho đến khi muốn kết thúc thì nhấn <finish>
my_dict = {}
while True: 
    key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish>: ")    
    if key == '<finish>':
        break
    else: 
        my_dict[key] = float(input('Enter value float của key mới nhập gần nhất: '))       
print(my_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
tich_values = 1
for key in my_dict:   # lần lượt lấy các key ra
    tich_values *= my_dict[key]                   # my_dict[key]: value key
print(f'Tích value của các phần tử trong một dict đã nhập là: {tich_values}')



'''
***Cách truy cập và duyệt trong dict***
- dict không có key thì chịu (các kiểu dữ liệu khác thì có index (trừ set ra))
- print(my_dict.get('game')) >>> get return None nếu key không tồn tại, 
còn print (my_dict['name']) sẽ trả lại lỗi
# _item = my_dict.items()    >>> ([('name', 'Một'), (2, [1, 2, 3]), ('age', 2)])  # convert sang list là okei. 
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

# # Khi biết trước n có thể tạo dict như sau: 
# my_dict = {}
# n = int(input('Enter n: ')) # nhập n key  ()
# for key in range(n):
#     key = input("Enter từng key (chú ý nhập value của key này ngay sau đây: ")    # Gán vào key (tạo tên key). 
#                                                                                 # Dict hay ở chỗ nếu key có rồi thì update, key chưa có thì tạo mới
#     my_dict[key] = float(input('Enter value float của key mới nhập gần nhất: '))      # Nhập value của key, 
# print(my_dict)
