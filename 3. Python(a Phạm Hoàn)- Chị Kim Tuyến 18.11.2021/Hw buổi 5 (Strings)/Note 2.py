'''
Bảng mã 256 kí tự ASCII từ 0 đến 255 (code)
Từ 32- 122 (khoảng trắng đến z ): trên bàn phím 
Tiếng việt: bộ gõ Unicode. 

Dấu cách có mã  32
Số 0-9 code:  48-57
A-Z : 65-90
a-z: 97-122    # cách nhau 32 đơn vị 

ord(): từ ký tự sang mã  (order) <> chr(): từ mã sang ký tự     character

So sánh 2 ký tự là ss bảng mã của nó. ( 'a' > 'A' >>> True , 'khan' > "Khang"      )
Interating: duyệt các ký tự trong chuỗi. 



'''
'''
#đếm số lượng ký tự số trong một chuỗi
# Cách 1 - dùng index để duyệt - duyệt gián tiếp > Dùng khi cần quan tâm chỉ số. 
s = input("Nhập chuỗi s: ")   
count = 0
for i in range(len(s)): 
  if '0' <= s[i] <= '9':    # ko phải ngôn ngữ nào cũng có đâu. 
    count += 1
print(count)


# Cách 2: Duyệt trực tiếp 
s = input("Nhập chuỗi s: ")
count = 0
for i in s: 
  if '0'<= i <= '9': 
    count +=1 
print(count)


#Task : 
Lấy tất cả các vị trí của ký tự 'a' trong chuỗi s
Cách 1: 
s = input("Nhập chuỗi s: ")  
count = 0
for i in range(len(s)): 
  if  s[i] == 'a':                
    print(i, end=' ')   
    
Cách 2: Có vẻ khá khó. 
s = input("Nhập chuỗi s: ")
for i in s: 
  if i == 'a':
    print(s[], end="\n")


'''
'''
s.upper() , s.lower(), s.sstrip, s.lstrip, s.rstrip()  và ko làm thay đổi s. 

Tìm kiếm và thay thế trong chuỗi: 
s.count(sub), s.find(sub): chỉ số của sub tính từ đầu, s.rfind(sub) : chỉ số của sub tính từ cuối
s.startswich("Py")   s.endswich("on") >>> True/ False

print(s.replace('y', 'i'))
print(s)     # s ko thay đổi. 
 
'''