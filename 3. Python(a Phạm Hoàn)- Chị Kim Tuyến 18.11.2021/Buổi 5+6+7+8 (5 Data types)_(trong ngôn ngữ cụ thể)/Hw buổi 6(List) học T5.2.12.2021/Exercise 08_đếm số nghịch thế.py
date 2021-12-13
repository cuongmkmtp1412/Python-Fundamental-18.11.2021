# Đoàn Ngọc Cường 6.12.2021- 18h 15 phút. 
'''
Bài 08. Cho list các số nguyên dương A.
Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn
A[i] > A[j] và i < j.
'''
# Đếm số nghịch thế- Nghịch thế có nhiều bài hay lém. 

n = int(input('Enter the number of integer of list = '))   # Số phần tử của inputed_list   
A = []                
for i in range(0, n):       
    A.append(input("Enter each number integer: ")  )     #Nhập vào list ban đầu

count_nghichthe = 0
# Ta cố định số ở vị trí i, và duyệt với các số ở vị trí từ i+1 đến hết,
# Nếu mà tích của (i-j)/ (A[i]- A[i]) âm thì cho ta một nghịch thế
for i in range(n): #truy cập chỉ số
    for j in range(i+1,n):    #Hàm range(start= 0, stop, step_size= 1)- ban đầu mình nhầm range((i+1):) 
        if (i-j)/(int(A[i])- int(A[j])) < 0 : # TypeError: unsupported operand type(s) for -: 'str' and 'str'
            count_nghichthe += 1
print(f'Số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn là: {count_nghichthe}')

    
"""
Nhận xét của anh Phạm Hoàn. 
Epsilon Bit6 thg 12   <Anh Hoàn>
việc tính toán thế này (i-j)/(int(A[i])- int(A[j])) < 0
sẽ phức tạp hơn so với so sánh
mà đặc biệt đã dùng đc for j in range(i+1, n) thì chỉ còn cần so sánh A[i] với A[j] là xong

Cường Đoàn Ngọc19:31
ui, e ngốc quá :V
"""