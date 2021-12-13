# Đoàn Ngọc Cường 8/12/2021
'''
Bài 04: Cho 1 list chứa các tuple không rỗng. 
Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]

# Đảo ngược list : list.reverse() method (thay đổi trực tiếp list ban đầu), 
# Sắp xếp list: list.sort() method (thay đổi trực tiếp list ban đầu) and
                sorted() function (giữ nguyên list ban đầu)  
inputed_list.sort() >>>print(inputed_list) >>> sort theo giá trị tăng dần 
inputed_list.sort(reverse = True)    >>> sort theo giá trị giảm dần. 
new_list = sorted(inputed_list)  print(input_list)  >>> list ban đầu vẫn giữ nguyên >>>print(new_list)
# A Tiến Lê 2021 hỏi mình 7/12/2021. 
'''
# Cách 1: Tách lấy các phần tử cuối của từng tuple con trong list, sắp xếp các phần tử cuối đó,
        # Rồi lại duyệt list ban đầu và tìm các tuple có phần tử thứ 2 theo thứ tự đã sorted.

given_list = [(2, 5), (4, 1), (0, 0), (3,5), (1,3,1)]    #Cho list chứa tuple không rỗng.
ele_fini_list = []     # danh sách chứa các phần tử cuối mỗi tuple.(element finish of list) 
for i in given_list: 
    ele_fini_list.append(i[-1])   
  
newl = sorted(ele_fini_list)      # hàm sắp xếp các phần tử cuối đó theo thứ tự tăng dần. 

out_put = []
for i in newl: #duyệt từng phần tử trong list đã sắp xếp
    for x in given_list:      #check các phần tử trong list ban đầu.
        if i == x[-1] and x not in out_put:      #chưa có trong out_put list mới thêm. 
            out_put.append(x)     
print(out_put)

# Cách 2 anh Hoàn chữa- cực kì hay ho luôn. 
# ý tưởng for i, rồi for j (chạy từ i+1) giống bài nghịch thế

list_sample = [(2, 5), (4, 1), (0, 0), (3,5), (1,3,1)]
for i in range(len(list_sample)):
    for j in range(i+1, len(list_sample)):
        if list_sample[i][-1] > list_sample[j][-1]:
            list_sample[i], list_sample[j] = list_sample[j], list_sample[i]
            # Cần sắp xếp từ bé đến lớn: Nên nếu a > b thì hoán đổi a, b = b, a
print(list_sample)
     
# Cách 3: dùng sort(key = ) # key là tiêu chuẩn chúng ta muốn so sánh. 

def get_list(x):
    return x[-1]

a_list = [(2, 5), (4, 1), (0, 0), (3,5), (1,3,1)]
a_list.sort(key=get_list)    # key: tiêu chuẩn cái chúng ta so sánh. 
# a_list.sort(key= lamda x: x[-1])    #function() đặc biệt: function lumda. 
print(a_list)

