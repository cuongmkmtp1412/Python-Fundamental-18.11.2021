# Đoàn Ngọc Cường
'''
Bài 06. Viết chương trình lấy ra top 3 phần tử có value lớn nhất từ dict
'''
# Tương tự như bài lấy ra top 3 có key lớn nhất. (Ctrl V sang rồi sửa)

# # Nhập dict: 
# my_dict = {}
# while True: 
#     key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish>: ")    
#     if key == '<finish>':
#         break
#     else: 
#         my_dict[key] = input('Enter value float của key mới nhập gần nhất: ')     
# print(my_dict)
# if len(my_dict) < 3:   # len() function: hàm chung, còn obj.method() gắn liền với obj 
#     print('Bạn cần nhập ít nhất 3 phần tử vào my_list')
#     quit()

my_dict = {'111': 3, '111': 2, '1111': 3, '111': 4, 'efdf': 5, 'f': 6}
dict_value = my_dict.values()    
list_value = list(dict_value)    

list_value.sort(reverse = True)    #  Ban đầu: list_value.sort(reversed) bị lỗi TypeError: sort() takes no positional arguments
top3_maxvalue = [list_value[0], list_value[1], list_value[2]]
print("top 3 phần tử của dict có key lớn nhất", end= ": ")
print()
for key in my_dict:
    if my_dict[key] in top3_maxvalue:
        print(my_dict[key], end=",")
print()