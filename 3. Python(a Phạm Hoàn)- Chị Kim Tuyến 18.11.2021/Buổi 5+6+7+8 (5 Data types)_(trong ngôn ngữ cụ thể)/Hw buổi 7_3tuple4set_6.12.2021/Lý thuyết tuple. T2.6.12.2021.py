'''
Rất ít ngôn ngữ có tuple - mean "một bộ".
Tuple khá giống list, chỉ khác ở chỗ là tuple khi đã khai báo thì ko thay đổi được ("nó giống string")
Giống list: Nhét cái gì vào cũng được. 
Ưu điểm : 
- Tạo ra các biến không cho người khác thay đổi được. Tuple giống list nhưng ko thay đổi được. 
- Cái quá trình for để duyệt tuple nhanh hơn dùng for để duyệt list. 

# Cách khai báo tuple có 1 phần tử. 
one_tuple = ('one') #  <=> 'one' >>> print(type(one_tuple)) >>> <class 'str'>
one_tuple = ('one',) >>> print(type_check_only(one_tuple))>>> <class 'tuple'>
'''
'''
#kĩ thuật Packing (đóng gói)- unpacking (bỏ gói): được phép bỏ ngoặc khi khai báo tuple: 
our_tuple = 'cat', '1999', 'money', 1992  # packing
print(our_tuple)
a, b, c, d = our_tuple     # unpacking.  # nếu thiếu nó báo: 
print(a)
print(b)   
'''
'''
Các phương thức của Tuple - rất ít: 
tuple.count(element) method
tuple.index(element) method : index của phần tử đầu từ trái sang phải. 
Còn các hàm chung thì vẫn có nhen: min(tuple), len(tuple) thì vẫn okei. 

- Duyệt cũng như string, list: có 2 cách: với for-in
love_tuple = ('HAT', 'MT', 'HNH', 'TH', '16Ty')
for i in love_tuple: 
    print(i)
for x in range(len(love_tuple)): 
    print(love_tuple[x])
'''


