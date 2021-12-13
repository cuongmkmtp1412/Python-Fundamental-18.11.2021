# Đoàn Ngọc Cường: 
'''
Bài 02. Viết chương trình tìm ra top 3 phần tử của dict có key lớn nhất
'''
# Nhập dict: 
my_dict = {}
while True: 
    key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish>: ")    
    if key == '<finish>':
        break
    else: 
        my_dict[key] = input('Enter value float của key mới nhập gần nhất: ')     
print(my_dict)
if len(my_dict) < 3:   # len() function: hàm chung, còn obj.method() gắn liền với obj 
    print('Bạn cần nhập ít nhất 3 phần tử vào my_list')
    quit()

# my_dict = {'111': 3, '111': 2, '1111': 3, '111': 4, 'efdf': 5, 'f': 6}
dict_key = my_dict.keys()    # nhìn giống list nhưng type: dict_key
list_key = list(dict_key)    # Bước 1: lấy ra list_key. 

list_key.sort()

# top_3_key = list(list_key[-1])+list(list_key[-2]) + list(list_key[-3]) # nếu ko có list thì là nối string, còn nếu có list thành ra list có các phần tử bị tách ra.
print("top 3 phần tử của dict có key lớn nhất", end= ": ")
for i in range(1,4): 
    print(f'{list_key[-i]}: {my_dict[list_key[-i]]}', end=',')





# DƯỚI NÀY LÀ COMMENT:

'''
Bảng mã 256 kí tự ASCII từ 0 đến 255 (code)
Từ 32- 122 (khoảng trắng đến z ): trên bàn phím 
Tiếng việt: bộ gõ Unicode. 
Dấu cách có mã  32
Số 0-9 code:  48-57
A-Z : 65-90
a-z: 97-122    # cách nhau 32 đơn vị 
'''

'''
Còn nếu mà sort theo độ dài key lớn nhất thì ta sort theo len(x)
def len_key(x):
    return len(x) 
list_key.sort(key=len_key)   # lấy ý tưởng từ bài về nhà 4 ở bài về nhà buổi 7. (buổi trước)
'''

'''
# Lấy idea từ bài này: 
Bài 04: Cho 1 list chứa các tuple không rỗng. 
Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]

# Cách 3: dùng sort(key = ) # key là tiêu chuẩn chúng ta muốn so sánh. 
def get_list(x):
    return x[-1]
a_list = [(2, 5), (4, 1), (0, 0), (3,5), (1,3,1)]
a_list.sort(key=get_list)    # key: tiêu chuẩn cái chúng ta so sánh. 
# a_list.sort(key= lamda x: x[-1])    #function() đặc biệt: function lumda. 
print(a_list)


'''
