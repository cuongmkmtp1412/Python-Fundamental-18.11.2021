#Đoàn Ngọc Cường 2/12/2021
'''
Bài 06. Viết chương trình
    1. Nhập vào 1 chuỗi từ bàn phím
    2. Nhập vào 1 ký tự từ bàn phím
    3. Tìm và in ra tất cả các vị trí của ký tự vừa nhập trong chuỗi đã nhập
'''
'''String: Chuỗi, Xâu: Là một chuỗi liên tiếp các ký tự
Ký tự: các chữ cái, các chữ số, dấu câu,...'''

str_input = input("Enter a string: ")
cha_input = input("Enter a character: ")
# Dùng index để duyệt các bài liên quan đến chỉ số. (Ko duyệt trực tiếp được)
for i in range(len(str_input)):
    if str_input[i] == cha_input:
        print(i)
    #print(str_input.find(cha_input)   : tìm chỉ số của sub tính từ đầu 
# Làm sao để print: "Các vị trí của ký tự vừa nhập là: ...."
