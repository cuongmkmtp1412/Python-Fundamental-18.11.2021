# Đoàn Ngọc Cường- chiều 13.12.2021- Bài tập cuối cùng (Từ 13h r- 17hr = 4 h xong 9 bài về nhà)
'''
Bài 09: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ
Ví dụ:
Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Output: {'item1': 1150, 'item2': 300}
Nếu Input: {'item1': 400}, 'item2': 300, 'item1': 750} thì item1 == 750 và bị mất đi value = 400 
>>> Ý nghĩa của bài tập này: 
        Khi mà khai báo 2 key cùng trong một dict thì key nhận value sau.
        Bài này giúp ta khai báo 2 key cùng trong một dict thì key nhận value tổng, 
        (ko làm mất các value trước đó)
'''
'''
# Thuật toán: 
- duyệt từng dict trong list. 
- Lấy value của key 'item' gán (=) vào new_key, và lấy value của key 'amount' cộng gán (+=) vào new_value.
''' 
# Phần 1: Nhập input từ bàn phím
inputed_list = []

while True: 
    my_dict = {}      # Ban đầu để my_dict ngoài vòng While nên bị lỗi chỉ ra mỗi dict cuối  : [{'item': 'i2', 'amount': 2.0}]
    value_item = input("Enter value_item (Chú ý: nếu key có rồi thì + thêm value và đến khi muốn dừng thì gõ <finish>: ")    
    if value_item == '<finish>':
        break
    else: 
        my_dict['item'] = value_item        # thêm vào my_dict 'item': 
        value_amount = input('Enter value_amount là một số thực')
        try: 
            value_amount = float(value_amount)
        except:
            print('Enter value mount must float type')
            continue
        my_dict['amount'] = value_amount     # thêm key-value: 'amount' : 
    inputed_list.append(my_dict)
    del my_dict         # # Ban đầu để my_dict ngoài vòng While nên bị lỗi chỉ ra mỗi dict cuối  : [{'item': 'i2', 'amount': 2.0}]
print(inputed_list)


# Phần 2: Thực hiện tìm output
# inputed_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output = {}
for my_dict in inputed_list:      #my_dict = {'item': 'item1', 'amount': 400}
    # print(my_dict['item'])        # item1
    # print(my_dict['amount'])      # 400
    # output[my_dict['item']] += my_dict['amount']     
    # Thêm vào output[key] += value (nếu có key thì +=, nhưng chưa có thì báo KeyError)
    if my_dict['item'] in output:     # in, not in chỉ check các key trong dict.
        output[my_dict['item']] += my_dict['amount'] 
    else:
        output[my_dict['item']] = my_dict['amount'] 
print(output)


'''
***PHÉP GÁN = THÊM MỚI/UPDATE CÁC PHẦN TỬ TRONG DICT***
# Khi ta cố gắng nhập 2 key cùng trong một dict thì dict sẽ lấy value nhập sau của key đó. 
# Có thể thay đổi / thêm mới dict, xoá dict (còn string, tuple thì ko thay đổi được). list và set thay đổi được. 
my_dict['a'] = 10  #thay đổi value của key age. 
my_dict['b'] += 2 # cập nhập value age thêm 2 đơn vị. ( Nếu chưa có key 'b' thì báo KeyError: 'b' )
my_dict['b'] = 'sdfdasfdsf'  # Khi key chưa tồn tại thì ta thêm mới
# cùng là toán tử gán, nhưng có 2 key: key đã tồn tại thì cập nhật, ngược lại thì thêm key mới vô. 
'''
'''
***CÁCH TRUY CẬP VÀ DUYỆT TRONG DICT***
- dict không có key thì chịu (các kiểu dữ liệu khác thì có index (trừ set ra))
- print(my_dict.get('game')) >>> get return None nếu key không tồn tại, 
còn print (my_dict['name']) sẽ trả lại lỗi
# _item = my_dict.items()    >>> ([('name', 'Một'), (2, [1, 2, 3]), ('age', 2)])  # type: dict_value not type: list 
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

