'''
***INTRODUCTION***
* set là tập hợp (như trong toán học) với các phép toán. 
* Mỗi phần tử là duy nhất ko trùng lặp, và ko có thứ tự.
* Trong python nó là: Các phần tử là bất biến ko thay đổi được 
* Các phần tử đặt trong ngoặc nhọn {}, cách nhau bởi dấu , 

* Chỉ chứa các phần tử với kiểu dữ liệu bất biến: int, float, string, tuple,.. ko chứa list, set, dict, ...
Morning = {'Morning', 3.14, (1, 2, 3, 'py')} >>> set là loại ko có thứ tự, lát print nó tự đảo thứ tự. 
>>> Cố tình tạo set chứa các phần tử trùng lặp >>> tự convert về dạng chuẩn. 
>>> Set ko bất biến, nhưng phần tử chứa trong nó phải bất biến. 
* Hệ quả: 
Cách truy cập: 
- MÌNH CỨ NGHĨ DÙNG CHỈ SỐ ĐỂ TRUY CẬP ĐƯỢC 
- TypeError: 'set' object is not subscriptable
- BUT, Không thể dùng khái niệm chỉ số để truy cập, VÌ nó ko hề có thứ tự. 
>>> Chỉ có một cách duỵet trong set là dùng : for-in '''


'''
***METHOD AND FUNCTION: ***
* Set thay đổi được (như list)- có tính update.
- dùng set.add() method thêm một phần tử 
- dùng set.update() method để thêm nhiều phần tử , có thể truyền vào string, list, tuple, set . Trùng lặp tự động loại bỏ
<<<list.append() method, and list.extend() method>>>
- Ba hàm xoá phần tử: 
set.discard(): ko báo lỗi khi phần tử ko có trong set. Còn set.remove() báo lỗi : KeyError 2000
set.pop() : xoá đi ở set phần tử bất kỳ, và trả giá trị đã xoá vào biến nào đó, z = set.pop() '''

'''
CHỐT LẠI CÁC METHOD() THAO TÁC VỚI 2 SET
    hơp, giao, bù, bù đối xứng 
    |, &, -, ^
    set_03 = set_01.union(set_02),  intersection, difference, symmetric_difference
    set_01.union_update(set_02) <=> set_01 = set_01.union(set_02) : gán/ update vào set_01, tương tự: ...

    # set.isdisjoint(other_set) return True if two sets are disjoint sets (is-dis-join) - tương tự isnumeric,...
    # set.issubset(other_set)    returns True if all elements of a set are present in another set
    # Ngược lại set.issuperset(other_set) method.  
      
'''

'''
***SỰ KHÁC NHAU CỦA METHOD() AND FUNCTION()***
- def function_name(parameter): - method - của object của class
- function không thuộc cái objcet nào. 
ex: 
- hàm len(), sin(), min(), max(), các hàm nằm lửng lơ một mình.
- sorted() function  - cung cấp chung
- list.sort() : cung cấp cho obj, class list. 
- set.pop() method: Nó tác động đến đối tượng set 
'''

# random.suffle()  rồi ta lấy ra 5 phần tử đầu tiên
# random.org thật là xác xuất thật, còn trang khác chỉ là giả thôi. 

# Thao tác chuyển đổi giữa các kiểu dữ liệu: 
app = set('apple')  # convert từ string sang set, tách từng phần tử của string 
for i in app: 
    print(i, end = '')   # >>> a, p, l, e

app_list = list('apple')    # tách từng kí tự ra, 
print(app_list)    #>>> ['a', 'p', 'p', 'l', 'e']
app_set = set(app_list)
print(app_set)