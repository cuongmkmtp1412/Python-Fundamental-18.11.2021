# Đoàn Ngọc Cường 2.12.2021
'''
Bài 01. Viết chương trình thay thế 
        tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
'''
str_input = input("Enter a string ")
str_replace = str_input.replace(str_input[0], "$")
print(str_replace)    

'''
str= 'phamphu'
z= str[0]+ str[1:].replace(str[0], '$')
print(z)

'''
