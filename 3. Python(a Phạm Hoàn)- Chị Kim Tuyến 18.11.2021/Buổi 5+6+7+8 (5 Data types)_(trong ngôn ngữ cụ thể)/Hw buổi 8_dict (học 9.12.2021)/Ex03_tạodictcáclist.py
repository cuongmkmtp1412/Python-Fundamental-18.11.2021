#Đoàn Ngọc Cường:13.12.2021
'''
Bài 03. Viết chương trình tạo ra dict với lớn hơn 3 phần tử,
value của mỗi phần tử là một list có lớn hơn 5 phần tử.
Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
'''
print('Bạn cần tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử')
my_dict = {}
while True: 
    key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish_key> hoặc <finish_dict>: ")    
    if key == '<finish_key>' or key == '<finish_dict>':
        if len(my_dict) > 3: break             # thoát vòng lặp
        else: 
            print('Dict cần có > 3 phần tử')
            continue               # Bỏ qua đoạn ở dưới và quay lại vòng lặp. 
    else: 
        list_value = []
        while True: 
            str_list = input("enter từng phần tử của list, kết thúc nhấn <finish_list>: ")  
            if str_list == '<finish_list>': 
                if len(list_value) > 5: break
                else: 
                    print('Bạn cần nhập > 5 phần tử cho list')
                    continue
            else:
                list_value.append(str_list)
        my_dict[key] = list_value                    # Chưa có key này nên là thêm mới.
print(my_dict)

# Bước thứ 2: Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
# my_dict = {'111': [1,2,3,4,5,6], 'cuong': [11,12,13,141,15,16]}
for key in my_dict:
    print(f'Từng phần tử thứ 5 trong phần value của mỗi phần tử trong dict là: {my_dict[key][4]}')


'''
# Khi chưa cần check điều kiện lớn hơn 3 phần tử trong dict với lớn hơn 5 phần tử trong list.
my_dict = {}
while True: 
    key = input("Enter key (Chú ý: nếu key có rồi thì update và đến khi muốn dừng thì gõ <finish_key> hoặc <finish_dict>: ")    
    if key == '<finish_key>' or key == '<finish_dict>':
        break
    else: 
        list_value = []
        while True: 
            str_list = input("enter từng phần tử của list, kết thúc nhấn <finish_list>: ")  
            if str_list == '<finish_list>': 
                break
            else:
                list_value.append(str_list)
        my_dict[key] = list_value                    # Chưa có key này nên là thêm mới.
print(my_dict)
'''

'''
Test cho vui: vì làm chắc từng bước thì ko cần test: 
{'cuong': ['1', '2', '3', '4', '5', '6'], 'Trà': ['4', '5', '6', '7', '8', '9', '4', '2', '2'],
'Yêu trà': ['1', '2', '', '654564', '6', '6', '5', '64', '6', '4<finish_list>'], 'fdsf': ['1', '6', '6', '74', '96', '4', '6', '14']}
Từng phần tử thứ 5 trong phần value của mỗi phần tử trong dict là: 5
Từng phần tử thứ 5 trong phần value của mỗi phần tử trong dict là: 8
Từng phần tử thứ 5 trong phần value của mỗi phần tử trong dict là: 6
Từng phần tử thứ 5 trong phần value của mỗi phần tử trong dict là: 96
'''