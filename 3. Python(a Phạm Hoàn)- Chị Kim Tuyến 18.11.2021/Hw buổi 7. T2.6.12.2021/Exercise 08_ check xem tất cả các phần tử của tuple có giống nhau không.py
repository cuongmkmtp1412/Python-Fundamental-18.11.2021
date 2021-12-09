# Đoàn Ngọc Cường 
'''
Bài 08: Viết chương trình kiểm tra xem 
tất cả các phần tử trong tuple có giống nhau hay không.
'''
# STEP 1: CÁCH INPUT TUPLE TỪ USER. 
n = int(input('Enter the number of elements of inputed tuple = '))
inputed_list = []  
for i in range(n): 
    inputed_list.append(input("Enter each element: "))  
inputed_tuple = tuple(inputed_list)     
# print(inputed_tuple)        
# print(type(inputed_tuple)) 

flag = True
for i in range(len(inputed_tuple)-1):   # truy cập chỉ số: trừ set. # ví dụ 1, 2, 3 thì kiểm tra 2 lần là xong.
    if inputed_tuple[i] != inputed_tuple[i+1]:   
        flag = False
        break

if flag == True: 
    print("Tất cả các phần tử của inputed_tuple là giống nhau.")
else: 
    print("Không phải tất cả các phần tử trong inputed_tuple là giống nhau.")

