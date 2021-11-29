#Đoàn Ngọc Cường - T2/29/11/2021
'''
Bài 07. Người dùng nhập vào số n - số hàng                             
để in mô hình kim tự tháp số dạng dọc như ví dụ sau: 
- Nếu nhập n = 3 thì in ra:
1
12
123
12
1
'''
def thap(i): 
    for x in range(1, i+1):
        print(x, end='')
n = int(input("Enter số nguyên dương n = "))
i = 1
while i < n : 
    thap(i)
    print()              #nếu ko có dòng này thì : 112123121. (để xuống dòng vì print("\n"))
    i += 1
while i >= 1: 
    thap(i)
    print()
    i -=1

