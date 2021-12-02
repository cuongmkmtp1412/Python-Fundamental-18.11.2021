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