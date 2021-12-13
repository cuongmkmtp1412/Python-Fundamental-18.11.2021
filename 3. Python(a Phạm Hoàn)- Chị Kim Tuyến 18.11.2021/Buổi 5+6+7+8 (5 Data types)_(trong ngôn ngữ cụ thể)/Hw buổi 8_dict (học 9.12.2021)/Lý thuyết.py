'''
- là tập hợp các phần tử, các phần tử đặt trong ngoặc nhọn {}, cách nhau bởi dấu (,) 
- Mỗi phần tử có dạng cặp key: value , biết key thì có thể truy xuất value
- value mang kiểu dữ liệu bất kì,
 key là những kiểu dữ liệu bất biến (string, number, tuple với các phần từ bất biến) và ko lặp
- Có thể thêm mới, thay đổi, cập nhật, xoá phần tử- quan tâm đến key
'''
my_dict = {       # key là các phần tử bất biến, ko trùng lặp để phân biệt các giá trị. 
    'name': 'Một',
    2: [1, 2, 3],
    # [1, 2, 3]: 'ba'
    'age': 2
}

'''
***PHÉP GÁN = THÊM MỚI/UPDATE CÁC PHẦN TỬ TRONG DICT***
# Khi ta cố gắng nhập 2 key cùng trong một dict thì dict sẽ lấy value nhập sau của key đó. 
# Có thể thay đổi / thêm mới dict, xoá dict (còn string, tuple thì ko thay đổi được). list và set thay đổi được. 
my_dict['a'] = 10  #thay đổi value của key age. 
my_dict['b'] += 2 # cập nhập value age thêm 2 đơn vị.  # Nếu chưa có key 'b' thì báo KeyError: 'b'
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

# dict comprehension: tạo dict một cách tôprng quats 
my_dict = {i: i**2 for i in range(10) if i % 3 == 0} # nhúng tất vô
print(my_dict)

my_dict = {}
for i in range(10): 
    my_dict[i] = i**2
print(my_dict)

# tạo ra các dict deform nó lớn: ví dụ yêu cầu tạo ra cái dict có 100 key. 
# tạo dữ liệu ban đầu thôi nha, Khi có dict rồi thì ko cần care. 
list_key = [1, -2, -4, -5, 3, 0, 2, 6]
list_value = [-1, 2, 4, -5, -3, 0, -2, 6] #value từ phải sang trái. 

my_dict = {}
for i in range(len(list_key)):  
    my_dict[list_key[i]]  = list_value[-i-1]
print(my_dict)
# hehe: gửi đầu tiên. mỗi tội bị phân tâm trong lúc học nên ko biết dạng comprehension là dạng gì. 

# Dạng dict comprehen: 
# my_dict = {k : v for  i in range(len(list_value))}
my_dict = { list_key[i] : list_value[-i-1] for i in range(len(list_value))}  
# comprehension: là dạng viết gọn lại thành một dòng như này. 
print(my_dict)

# dictionary cực quan trọng khi thời đại chúng ta đang làm việc với dữ liệu 
# Json: có dạng giống dictionary 
# truyền dữ liệu từ server  xuống cho máy nền show ra trên trình duyệt, nó ở dạng text (json), ta convert từ dict sang json và ngược lại 
# để làm việc trong python, 
# giá trị đó tương ứng với key gì, nhìn vào là biết. 
# Một danh bạ, thường lưu trữ dữ liệu ở dạng dictionary, 
a_contact = {
    'first_name':   'Phạm',
    'last_name' :   'Hoàn'                         # sau list thì dictionary ứng dụng cực kì nhiều

}


'''
Vài cái khác- phụ và ko quá quan trọng
Xoá bỏ: truyền key muốn xoá vào hàm pop(), xoá xong trả lại value vào hàm đó
popitem() : xoá đi phần tử cuối
clear: xoá hết, del xoá phần tử cụ thể
# v = my_dict.pop('age') # v nhận giá trị của 12
# idem = my_dict.popitem()  # idem dạng tuple: (key, value)
# my_dict.clear()  # print(my_dict)  >>> {} set rỗng. 
v = my_dict.get(10, -10)   # 10 ko tồn tại thì trả lại giá trị -10
v_ = my_dict.get('age', -10)   # age có tồn tại thì in giá trị của age
print(v)
print(v_) 
# v= my_dict.pop(10) # báo lỗi đo
# v= my_dict.pop(10, "no key")  # ko có thì trả lại "no key"


# cố định tạo ra 2 key trong một dict, thì dict sẽ thực hiện lấy value cuối của key đó
# Điều này làm ta mất dữ liệu trước đó đi. 

# key là các phần tử bất biến, ko trùng lặp để phân biệt các giá trị. 

# my_dict.update({
#     1: "10", 
#     'name': 2
# })

# my_dict = {}.fromkeys([1, 3, 5])  # tất cả được gán value = None
# my_dict = {}.fromkeys([1, 4, 5], "value chung")

# z = my_dict.setdefault(0)    # đặt cách nhập ở 0,0 # thêm vào phần tử 0, (nếu có rồi thì trả về value, chưa có trả về None)
# z = my_dict.setdefault(0,0) # update xong rồi get, ko thêm mới được phần tử thì get luôn. 

# # in, not in chỉ check được cái key thôi, return True nếu tồn tại. 

'''


