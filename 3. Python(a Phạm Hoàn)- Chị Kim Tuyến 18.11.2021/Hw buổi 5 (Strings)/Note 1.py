'''
String: Chuỗi, Xâu: Là một chuỗi liên tiếp các ký tự
Ký tự: các chữ cái, các chữ số, dấu câu,...
Chuỗi được tạo ra :    
- nhập từ bàn phím với hàm input()  #n = input()   # input vào thì luôn là string
- khai báo trong cặp nháy đơn, cặp nháy kép, cặp 3 nháy đơn, hoặc 3 nháy kép
- Là kết quả cộng chuỗi, nhân chuỗi với số 
- Ép kiểu bằng str()
- Đọc từ file ra 
# my_string_03 = """hello
I am Cuong
Nice to meet you"""
# Ba nháy đơn hoặc ba nháy kép > string mà có nhiều dòng. 

'''
'''
2 phép toán: -Cộng 2 chuỗi = nối 2 chuỗi
               -Nhân một chuỗi với một số nguyên dương
'''
 




'''Accessing Strings: 
- Truy cập từng ký tự dùng index : từ 0 đến len(s)-1, từ -len(s) đến -1
- hoặc một đoạn ký tự bằng đoạn cắt (slicing) 
#print(s[a])
s = "python olala!"
print(s[100])   #IndexError: string index out of range , còn print(s[2 : 150]) thoải mái
print(s[-100])  #IndexError: string index out of range
min = -len(s), max = len(s) - 1 
print(s[len(s)-1]) >>> mình cmt là n >>> ngu ngốc >>> ra ! (là ký tự cuối cùng)

# print([a:b])   Nếu ko tồn tại thì nó hiện rỗng, chứ ko lỗi gì cả= range. 
print([1:5])          print(s[-9 : -1])      print(s[5: -3])  
print(s[:3])     print(s[4:])       print(s[:])
print(s[:-3])     print(s[-4:])       print(s[:])   #(Từ đầu đến s[-3] và từ s[-4] đến hết cuối. )

#Kỹ thuật cắt chuỗi - Slicing - Nâng cao - Cắt với bước nhảy gióng range(a, b, c)
print(s[i:j:a])   a nhận cả - và + tương tự range(). Khi a âm thì xét dãy từ cuối lên đầu. 
s = "0123456789"
print(s[2:-1:3])
print(s[::2])  print(s[1::2])      print(s[:2:2])         print(s[1:100:2])
print(s[::2])    print(s[-1::2])      print(s[:-2:2])    (Từ s[-1] đến hết cách nhau 2, từ đầu đến s[-2] cách nhau 2, )
print(s[::-2])    print(s[-1::-2])      print(s[:-2:-2])  (Từ -1 lộn lên hết đầu, cách nhau -2, và từ cuối lộn lên đến s[-2, và cách nhau 2.])
# hay đấy- đảo chuỗi hay đó, (trước mình mất công chuyển sang list rồi đảo list và )

# Không thể Change or Delete Chuỗi: 
String are immutable
s="python"
s[1]= "i"   # TypeError: 'str' object does not support item assignment

'''