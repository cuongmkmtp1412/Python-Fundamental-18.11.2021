#Đoàn Ngọc Cường 9/12/2021
'''
Bài 09: Viết chương trình tính tổng
 và tìm giá trị lớn nhất trong tuple chứa các số thực.
'''
# STEP 1: INPUT TUPLE chứa các số thực TỪ USER. 
# Step 2: tính tổng các số thực của tuple. 

n = int(input('Enter the number of float numbers of inputed_tuple = ')) # Bỏ qua việc kiểm tra n từ người dùng. 
inputed_list = []  
while len(inputed_list) < n:      
    #for i in range(n):  Khi dùng for- continue thì có thể không đủ n phần tử/
    #for-break thì phải nhập lại từ đầu. 
    enter_float = input("Enter each float number: ")
    try: 
        enter_float = float(enter_float)
        inputed_list.append(enter_float)  
    except: 
        print("Ký tự bạn vừa nhập không phải là số thực (float). Hãy nhập lại")
        # continue
inputed_tuple = tuple(inputed_list)     
print(f'Tuple chứa {n} số thực đã nhập  là: {inputed_tuple}')        
# print(type(inputed_tuple))
print(f'Tổng của {n} số thực trong tuple đã nhập là: {sum(inputed_tuple)}')
print(f'Số thực lớn nhất trong {n} số thực của tuple đã nhập là: {max(inputed_tuple)}')

