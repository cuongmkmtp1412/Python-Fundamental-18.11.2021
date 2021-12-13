#Đoàn Ngọc Cường- T2-29/11/2021
'''
Bài 06. Nhập vào một số tự nhiên x, 
        tìm số n lớn nhất mà tổng các số tự nhiên đến n không vượt quá x
'''
x = int(input("Nhập số tự nhiên x = ")) # số thực cũng được 
sum = 0
n = 0
while sum <= x:           # chú ý các đầu mút khi thiết lập điều kiện
    n += 1
    sum += n
print(f'Số nguyên dương n lớn nhất mà tổng các số tự nhiên đến n không vượt quá {x} là {n-1}')
# Hôm ở trên lớp cứ nghĩ theo hướng làm vòng lặp for, lú cả đầu => ko ra. 