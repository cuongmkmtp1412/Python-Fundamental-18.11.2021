'''
Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
'''
# STEP 1: CÁCH INPUT TUPLE TỪ USER. 
# Giống như list, ta có thể input từng element vào tuple và lưu trữ từng element dưới dạng string.
n = int(input('Enter the number of elements of inputed tuple 01 = '))
inputed_list_01 = []  # tuple như list nhưng không thể thay đổi khi đã khai báo.
for i in range(n): 
    inputed_list_01.append(input("Enter each element of tuple 01: "))  #Giống list: Nhét cái gì vào cũng được. 
inputed_tuple_01 = tuple(inputed_list_01)    # chuyển từ list đã khai báo thành tuple. 
print(inputed_tuple_01)        #("[1, 'cuong']", "(1, 'cuong')")
print(type(inputed_tuple_01))     #<class 'tuple'>, và các elements trong tuple này đều ở dạng string, chú ý chuyển đổi nếu cần dùng. 

n = int(input('Enter the number of elements of inputed tuple 02 = '))
inputed_list_02 = []  
for i in range(n): 
    inputed_list_02.append(input("Enter each element of tuple 02: "))  
inputed_tuple_02 = tuple(inputed_list_02)     
print(inputed_tuple_02)        
print(type(inputed_tuple_02))    

# STEP 2: CHECK XEM 2 TUPLE CÓ PHẦN TỬ CHUNG KHÔNG.(giống bài kiểm tra 2 list hôm nọ)

flag = False  #Nếu 2 chuỗi ko có phần tử chung thì là False

for i in inputed_tuple_01: 
    if i in inputed_tuple_02: 
        flag = True
        break     #Anh Phạm Hoàn: tối ưu là khi flag = True, nên break luôn
if flag == True: 
    print("2 tuple đã nhập có phần tử chung")
else: 
    print("2 tuple đã nhập ko có phần tử chung")   
# Chặt hơn thì in ra tất cả phần tử chung của 2 tuple. 
