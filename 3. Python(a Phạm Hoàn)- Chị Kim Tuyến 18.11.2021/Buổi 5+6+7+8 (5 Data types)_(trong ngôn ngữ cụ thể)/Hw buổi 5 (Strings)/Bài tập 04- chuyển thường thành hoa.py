# @Đoàn Ngọc Cường - 2.12.2021
'''
Bài 04. Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa
 và từ ký tự hoa sang ký tự thường trong một chuỗi.
'''

str_input =  input("Enter a string: ")
for i in str_input: 
    if i.isupper() is True:    #x.islower() method, x.isupper() method  (True- false)
        i = i.lower()          #s.lower () method     
    else: 
        i = i.upper()
    print(i, end="")    #-sep: Phân tách các giá trị cần print(Mặc định khoảng trắng)
                        # -end: Kết thúc sau khi print (Mđ: '\n')
print()             # print() để trong vs code xuống dòng nhìn cho đẹp. 
                    #str_input không hề thay đổi

# Điểm chỉ được 300/500: Đề yêu cầu ghép các ký tự thành string mới rồi mới print- chứ ko phải print các ký tự. 
# sửa 
str_input =  input("Enter a string: ")
temp_str = ""
for i in str_input: 
    if i.isupper() is True:    
        temp_str += i.lower()           
    else: 
        temp_str += i.upper()
print(temp_str)

'''
@Phạm Hoàn
Trong khi lập trình. In ra luôn luôn chỉ là phụ.
Kiểu để debug, để thấy đc kết quả như nào thôi
In ra chỉ là để show ra xem nó thế nào.
'''