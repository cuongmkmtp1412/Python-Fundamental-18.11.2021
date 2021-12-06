'''
Bài 10.
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
'''
#Đếm số phần tử phân biệt trong list. 

n = int(input('Enter the number of songs: N = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter ID of each song: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu
count = 0    # Độ dài list dài nhất chứa các  ID phân biệt. 
out_list = []
for i in inputed_list: 
    if i not in out_list: 
        out_list.append(i)   # list.append() method
        count +=1
print(f'List dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại là: {out_list}')        
print(f'Độ dài của list dài nhất chứa các bài hát phân biệt là: {count}')