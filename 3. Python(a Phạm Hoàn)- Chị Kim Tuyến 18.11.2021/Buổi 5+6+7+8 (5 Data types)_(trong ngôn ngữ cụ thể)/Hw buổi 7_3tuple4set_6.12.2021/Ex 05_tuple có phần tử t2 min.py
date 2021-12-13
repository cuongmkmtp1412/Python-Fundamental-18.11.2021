#Đoàn Ngọc Cường: đêm t4.8.12.2021  # để dấu gạch chéo là lỗi: 
# Khi mình đặt tên tệp quá dài, với nhiều kí tự hỗn loạn >>> Bị như này
#7. T2.6.12.2021 (Kiß╗âu dß╗» liß╗çu thß╗⌐ 3-tuple v├á 4- set). 
# Hß╗ìc T2.6.12.2021/Exercise 05-tuple c├│ phß║ºn tß╗¡ thß╗⌐ 2 l├á nhß╗Å nhß║Ñt , tß╗½ mß╗Öt list chß╗⌐a c├íc tuple_ List nhß║¡p nhanh tß╗½ b├án ph├¡m.py':
# [Errno 2] No such file or directory
'''
Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất
, từ một list chứa các tuple.
'''

# Enter list các tuple bằng việc nhập các thứ đơn lẻ từ bàn phím.
n = int(input('Enter the number of elements of inputed list = '))
inputed_list = []  
for i in range(n): 
    # inputed_list.append(tuple(input("Enter each tuple) : "))) #>> (('1', ',', ' ', '2'), ('1', ',', ' ', '2')) . Chuyển từng kí tự khai báo sang tuple 
    # inputed_list.append(input("Enter each tuple) : "))  #>>('1, 2', '1, 2', '1, 2') #Giống list: Nhét cái gì vào cũng được.    
    m = int(input(f'Số lượng phần tử của tuple con thứ {i+1} = '))
    new_list = []
    for j in range(m): 
        # 6 dòng trên chia thành 2 cụm giống hết cấu trúc.       
        new_list.append(input(f'Enter phần tử thứ {j+1} của tuple con {i+1}: '))
    new_tuple = tuple(new_list) #chuyển các phần tử đã nhập vào new_list sang tuple
    inputed_list.append(new_tuple)   #ghép các tuple vào inputed_list
    del new_list                     #xoá new_list để chuẩn bị cho i tiếp theo. 
print(f'List chứa các tuple con đã nhập là: {inputed_list}') 
# inputed_list = [( '1'), ('1', 'Cuong'), ('1', 'cuong', '3')]


# Bước 2: tìm ra tuple có phần tử thứ 2 là nhỏ nhất
index_2_list = [] #list chứa các phần tử thứ 2 của mỗi tuple. 
for tuple in inputed_list: #duyệt từng phần tử của inputed_list, # for tuple thay vì for i như ban đầu. 
    if len(tuple) >=2:   #Tránh lỗi: IndexError: tuple index out of range
        index_2_list.append(tuple[1]) # tuple có các chỉ mục như list, string
if len(index_2_list) >= 1:  # Thêm câu lệnh này để tránh việc các tuple đều không đủ 2 phần tử. 
    min_index_2 = min(index_2_list)    #số < chữ Hoa < chữ thường.
# print(min_index_2)   #cmt để check

print("Tuple có phần tử thứ 2 là nhỏ nhất, từ list ban đầu là: ")
for tuple in inputed_list:
    if len(tuple) >= 2 and tuple[1] == min_index_2:
        #print(f'Tuple có phần tử thứ 2 là nhỏ nhất, từ list ban đầu là {tuple}')
        print(tuple, end = ',')
print()  #để trên vs code, output ko dính liền với đường dẫn thư mục. 

'''
Những thứ hiện ra khi run program : 
List chứa các tuple con đã nhập là: [('1',), ('1', 'cuong'), ('2', 'cuong', '4')]
Tuple có phần tử thứ 2 là nhỏ nhất, từ list ban đầu là:
('1', 'cuong'),('2', 'cuong', '4'),
Dành hơn 1 tiếng để làm khá hoàn thiện bài này:
- từ việc giúp người dùng nhập nhanh dữ liệu
- đến việc kiểm soát các trường hợp xảy ra
- đến việc nghĩ cách print() cho đẹp khi có nhiều hơn 1 tuple thoả mãn đề bài.
'''


