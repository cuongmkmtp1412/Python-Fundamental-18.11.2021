# Nọ nghỉ một buổi đi thi nên 11 h xem lại, ăn xong xem lại tiếp và code đến 6hr liên tục, ko nghỉ quá 15 phút. 
'''
Giới thiệu:
- Tần xuất dùng trong Python nhiều nhất. 
- Nhét cái gì vào trong list cũng được (Ko nhất thiết chỉ là kí tự như string. Nhét được nhiều thứ sau này chúng ta học.)
'''

'''
our_list = [ 0, 'tra', [1, 2, 3], [1, 2, 'cuong', 'tra']]
empty_list = []  #Hoặc _empty_list = list()  l>>> []  list rỗng- như string rỗng = ''  
print(our_list[3][[2]])   # truy cập vào phần từ index = 2 trong phần tử index = 3 của ourlist. 
'''

'''Phép toán với list: Cộng và nhân 2 list như với string'''

'''
# Các method của list: 
#String are immutable (no change and no delete), but List is mutable.   
s="012345"   s[1]= "i"   # TypeError: 'str' object does not support item, 
Hoặc khi s[1].upper() thì khi print(str_input) thì str_input vẫn ko thay đổi.
inputed_list = [0, 1, 2, 3, 4, 5]   inputed_list[1:3] = [10, 20, 30]  print(input_list)>>> [0, 10, 20, 30, 4, s]  

#Thêm mới 1 phần tử = list.append() method / thêm mới nhiều phần tử = list.extend() method.  
inputed_list.append([-1, -2, -3])   >>> [0, 1, 2, 3, 4, 5,[-1, -2, -3]] 
inputed_list.extend([-1, -2, -3])   >>> [0, 1, 2, 3, 4, 5, -1, -2, -3]
#Chèn thêm vào vị trí bất kì = insert(index, value) function. 
inputed_list.insert(2,20)  >>>> [0, 1,20, 2, 3, 4, 5]

#Xoá 1/ nhiều phần tử = toán tử del list() , list.remove() method, list.pop() method, list.clear() method. 
del input_list([2:4 ]) 
inputed_list.remove(8), xoá phần tử đầu tiên từ trái sang phải, nếu phần tử muốn xoá ko thuộc list ban đầu thì Traceback.
inputed_list.pop(5)  <=>   del inputed_list.pop(5)    , mặc định pop() xoá phần tử cuối. 
x = inputed_list.pop(5)   # xoá phần tử ở vị trí thứ 5 và gán giá trị đã xoá vào x. 
inputed_list.clear()  >>> print(inputed_list)   >>> []

# Đảo ngược list : list.reverse() method (tác động trực tiếp vào list luôn), sắp xếp list: list.sort() method (thay đổi trực tiếp list ban đầu) and sorted() function (giữ nguyên list ban đầu)  
inputed_list.sort() >>>print(inputed_list) >>> sort theo giá trị tăng dần 
inputed_list.sort(reverse = True)    >>> sort theo giá trị giảm dần. 
new_list = sorted(inputed_list)  print(input_list)  >>> list ban đầu vẫn giữ nguyên >>>print(new_list)

#list.copy() method:      
copy_list = input_list.copy()   >>> print(copy_list)>>>     

### NHẮC LẠI : kHI HỌC THÌ NHIỀU CÁI LINH TINH, CÒN KHI LÀM THÌ CHÚNG TA CẦN CÁI J THÌ CHÚNG TA ĐI TÌM HIỂU NÓ- SEACH GG NÓ- HỎI MN VỀ NÓ. 
(SEARCH LÀ KĨ NĂNG QUAN TRỌNG NHẤT MÀ LẬP TRÌNH VIÊN CẦN CÓ)

'''
'''
# Kiểm tra sự tồn tại: in, not in
# Duyệt list:   for i in range(len(inputed_list)):  #duyệt qua chỉ số 
                for i in inputed_list:              #duyệt trực tiếp

# # LIST COMPREHENSION = cách nhập từng phần tử vào
# n = int(input('Enter n = '))    # Khi bài toán yêu cầu input list = ...
# input_list = []                #ta sẽ enter từng string vào và append thành list
# for i in range(0, n): 
#     str_input = input("Enter strings")
#     input_list.append(str_input)
# print(input_list)
'''
##Task 1: sinh ra list chứa bình phương các số tự nhiên từ 0 đến n: 

##Cách 1: 
# n = int(input('Enter n = '))   
# output_list = []               
# for i in range(0, n+1): 
#     output_list.append(i**2)
# print(output_list)

# #Cách 2: 
# n = int(input("Enter n = "))
# output_list = [i**2 for i in range(0, n+1)]   # for lồng for cũng được. 
# even_list = [i for i in range(0, n+1) if i % 2 == 0]     # gọn và clear. 
# print(output_list)
# print(even_list)







