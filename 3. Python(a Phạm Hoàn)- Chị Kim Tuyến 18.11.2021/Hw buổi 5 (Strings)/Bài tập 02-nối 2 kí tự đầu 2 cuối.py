#Đoàn Ngọc Cường 2.12.2021
"""
Bài 02. Viết chương trình 
        sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
        nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
"""
str_input = input("Enter a string: ")
if len(str_input) >= 2: 
    print(f'Chuỗi từ 2 ký tự đầu và 2 ký tự cuối là: {str_input[0:2] + str_input[-2:]}')
else:
    print("Chuỗi rỗng")