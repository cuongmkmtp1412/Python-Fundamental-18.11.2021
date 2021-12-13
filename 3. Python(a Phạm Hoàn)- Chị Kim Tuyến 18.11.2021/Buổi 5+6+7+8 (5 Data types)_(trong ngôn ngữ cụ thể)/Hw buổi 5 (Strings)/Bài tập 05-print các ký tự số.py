#Đoàn Ngọc Cường 2.12.2021
'''
Bài 05. Viết chương trình in ra các ký tự số trong chuỗi được nhập từ bàn phím
'''
str_input = input("Enter a string: ")
for i in str_input: 
    if i.isnumeric() is True:       #chú ý không để thiếu ()
        print(i, end=" ")
print()                   #Dòng này để print trong vs code cho đẹp.
#Làm sao để print: "Các ký tự số trong chuỗi vừa nhập là: ...." 

#hoặc Cách 2 : 
flag = False    #  Có thể thay True = 0, 1, 2 tuỳ ý hoặc count = 0 # ko có ký tự số. 
for i in str_input:
    if '0' <= i <= '9':
        flag = True     # count =+ 1
        print(i, end='')
if flag == False:         #count == 0 
    print("No have number")
