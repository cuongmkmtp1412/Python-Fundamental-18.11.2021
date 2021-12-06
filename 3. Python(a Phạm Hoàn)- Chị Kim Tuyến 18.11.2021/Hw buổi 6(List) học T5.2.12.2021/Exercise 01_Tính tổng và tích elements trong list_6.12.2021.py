'''
Bài 01. Viết chương trình tính tổng, tích của các phần tử trong một list.
'''
n = int(input('Enter the number of elements of inputed_list = '))   # Số phần tử của inputed_list 
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

sum = 0
mul = 1
flag = False  # Để kiểm soát việc ko có số nào trong list.
for i in inputed_list:
    #if  '0' <= i <= '9':   # ValueError: could not convert string to float: '2fsf'
    #if i.isnumeric() :     # chỉ kiểm soát được các số int, float nó bỏ qua
    try: 
        i = float(i)
        flag = True
    except: 
        continue
    sum += float(i)
    mul *= float(i)
if flag == False: 
    print("Không có số float nào trong list để thực hiện tính tổng hoặc tích")
if flag == True:
    print(f'Tổng của các phần tử trong list là:{sum}')
    print(f'Tích của các phần tử trong list là: {mul}')