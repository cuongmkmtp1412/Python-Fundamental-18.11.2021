#Đoàn Ngọc Cường- 27/11/2021
'''
Bài 01. Lập chương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kì từ bàn phím
    2. Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  
    (Xét tất cả các trường hợp có thể xảy ra)
'''
import math
a, b, c = float(input("Enter number a = ")), float(input("Enter number b = ")), float(input("Enter number c = "))
delta= b**2-4*a*c
if delta > 0: 
    print(f"Phương trình có 2 nghiệm phân biệt là : x_1 = {(-b + math.sqrt(delta))/(2*a)} và X_2 = {(-b - math.sqrt(delta))/(2*a)}")
elif delta == 0:
    print(f'Phương trình có nghiệm kép x_1= x_2 = {-b/(2*a)}')
else: 
    print(f"Phương trình có 2 nghiệm phức phân biệt là x_1 = {complex(-b,math.sqrt(-delta))/(2*a)} và x_2 = {complex(-b,-math.sqrt(-delta))/(2*a)} ")

#bài đầu tiên từ khi học anh Hoàn đến giờ ko được điểm full, chỉ được 300/500. 
#Thiếu trường hợp a == 0 một cách ngu ngốc. 