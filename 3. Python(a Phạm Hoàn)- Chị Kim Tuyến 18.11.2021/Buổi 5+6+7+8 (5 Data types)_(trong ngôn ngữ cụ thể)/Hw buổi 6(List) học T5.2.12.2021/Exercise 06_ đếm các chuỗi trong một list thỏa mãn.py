'''
Bài 06. Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
'''
n = int(input('Enter the number of elements of list = '))   # Số phần tử của inputed_list   
inputed_list = []                
for i in range(0, n): 
    _input = input("Enter each element: ")          
    inputed_list.append(_input)     #Nhập vào list ban đầu

count = 0           #list.count(obj) là đếm số lần xuất hiện của một chuỗi trong list
for i in inputed_list:      # Đếm thì nên duyệt chỉ số.
    if len(i) >= 2 and i[0] == i[-1]: 
        count +=1
print(f'các chuỗi trong một list thỏa mãn đề bài là: {count}')
# Các chuỗi giống nhau nếu lặp lại thì vẫn được đếm.
