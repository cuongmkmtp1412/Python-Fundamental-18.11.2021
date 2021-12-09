# Đoàn Ngọc Cường 
'''
Bài 10: Cho list sau:
["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"].
Viết chương trình để in ra hậu tố (vn, org, net, com)
trong các tên miền website trong list trên.
'''
'''
# Tương tự như assignment 2/ chapter7/ course 2/ coursera: Tách số 0.8475 ra. 

#Cách 2: anh Phạm Hoàn gợi ý dùng split string và mình triển. 
str_input = "X-DSPAM-Confidence:    0.8475"

list_input = str_input.split(' ')   #  ['X-DSPAM-Confidence:', '', '', '', '0.8475']
for i in list_input:
    try:
        i = float(i)
    except: 
        continue
    print(i)
#Tách thử cái này ? 'Cho một đống số:10.256,16.356,13.265' 
(Giả sử người nhập làm ẩu ko để khoảng trắng ở giữa.)
'''

inputed_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
# Thuật toán: Duyệt từng phần tử, split(.) tạo vào new_list, rồi duyệt new_list[-1], ghép vào chung một list khác rồi print. 

outputed_suffix_list = []     #Khởi tạo list chứa các hậu tố cần gom, lát print- output

for i in inputed_list:    # i là từng string
    new_list = i.split('.')  # cắt {i} theo . và tạo thành new_list  # str.split() method không làm thay đổi string ban đầu
    outputed_suffix_list.append(new_list[-1])   # lấy phần tử cuối của new_list gom vào outputed_suffix_list  

print("Hậu tố trong các tên miền website của list đã cho là: ", end = "")  # Không muốn xuống dòng, 
for i in outputed_suffix_list: 
    print(i, end=", ")
print() # để trên vs code: output ko dính liền với PS C: 
# Output: Hậu tố trong các tên miền website trong list đã cho là: vn, org, net, com, 