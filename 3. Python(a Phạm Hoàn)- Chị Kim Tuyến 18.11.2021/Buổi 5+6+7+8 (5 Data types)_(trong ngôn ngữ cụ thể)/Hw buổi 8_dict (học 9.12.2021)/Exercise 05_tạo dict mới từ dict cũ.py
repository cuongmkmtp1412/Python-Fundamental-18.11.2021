# Đoàn Ngọc Cường - 13.12.2021
'''
Bài 05. Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu
 theo tập các key cho trước. 
Ví dụ:
dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
Output: {'name': 'Kelly', 'salary': 8000}
'''

original_dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
given_keys = ["name", "salary"]
output_dict = {}
for key in original_dict:
    if key in given_keys:    # in, not in chỉ check được cái key thôi, return True nếu tồn tại. 
        output_dict[key] = original_dict[key]    
        # my_dict['key'] = "10" nếu chưa có thì thêm, có rồi thì update
print(output_dict)