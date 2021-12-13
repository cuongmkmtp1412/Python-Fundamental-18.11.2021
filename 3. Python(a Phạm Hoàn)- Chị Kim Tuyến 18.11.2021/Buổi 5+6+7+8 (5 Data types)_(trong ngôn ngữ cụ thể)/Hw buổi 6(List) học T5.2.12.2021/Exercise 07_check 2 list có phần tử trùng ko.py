'''
Bài 07. Viết chương trình kiểm tra 2 list có phần tử chung hay không.
'''
n = int(input('Enter the number element of list1 = '))   # Số phần tử của inputed_list   
inputed_list1 = []                
for i in range(0, n): 
    _input = input("Enter each element of list1: ")          
    inputed_list1.append(_input)     #Nhập vào list ban đầu

n = int(input('Enter the number of elements of list2 = '))   # Số phần tử của inputed_list   
inputed_list2 = []                
for i in range(0, n): 
    _input = input("Enter each element of list2: ")          
    inputed_list2.append(_input)     #Nhập vào list ban đầu

flag = False  #Nếu 2 chuỗi ko có phần tử chung thì là False

for i in inputed_list1: 
    if i in inputed_list2: 
        flag = True
if flag == True: 
    print("2 list đã nhập có phần tử chung")
else: 
    print("2 list đã nhập ko có phần tử chung")   

# Chặt hơn thì in ra Phần tử chung của 2 chuỗi. <Nhưng mệt quá rồi> < 7h liên tục. > 
'''
Nhận xét của anh Phạm Hoàn 8.12.2021
2 nhận xét riêng tư
Epsilon Bit6 thg 12
tối ưu là khi flag = True, nên break luôn
Cường Đoàn Ngọc19:46
Dạ vâng ạ, hihi.



'''