# Đoàn Ngọc Cường
'''
Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
Input: ‘Stringings’
Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
'''
#  str/tuple.count(element) method - string và tuple đều ko thay đổi được khi đã khai báo.

string = 'Stringings'
output = {}    # tạo tuple output rỗng, 
# idea key: duyệt từng từ của string 
# idea value: dùng count() (có tuple.count() method, string.count(),  )
for i in string: 
    output[i] = string.count(i)

print(output)

'''
Ban đầu mình dùng: # tuple.count() method ra ngon.

string = 'Stringings'
output = {}    # tạo tuple output rỗng, 
# idea key: duyệt từng từ của string 
# idea value: dùng count() (có tuple.count() method, )
tuple_string = tuple(string)
print(tuple_string)
for i in string: 
    output[i] = tuple_string.count(i)
print(output)
'''

'''
str.count(sub, start= 0, end=len(string)) method  . String và tuple đều ko thay đổi được. 
Các tham số:
    sub: Đây là chuỗi con để được tìm kiếm.
    start: Tìm kiếm bắt đầu từ chỉ mục này. 
        Ký tự đầu tiên bắt đầu từ chỉ mục 0. Theo mặc định, bắt đầu tìm kiếm từ chỉ mục 0.

    end: Tìm kiếm kết thúc tại chỉ mục này. 
        Theo mặc định, việc tìm kiếm kết thúc ở chỉ mục cuối cùng.
'''