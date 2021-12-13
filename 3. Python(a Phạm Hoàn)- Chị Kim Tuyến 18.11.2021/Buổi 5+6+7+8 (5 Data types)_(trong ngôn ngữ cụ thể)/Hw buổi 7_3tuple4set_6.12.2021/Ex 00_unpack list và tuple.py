# Đoàn Ngọc Cường- Tối T4/8/ 12/2021. 
'''
https://classroom.google.com/u/0/c/NDM1NTgzOTIwODcx/a/NDQyMjcyMjg3Nzk4/details
Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
Sau đó, unpack các phần tử trong một tuple.
'''
our_tuple = 1, '1', 'cuong', [1, '1', 'cuong'], (1, '1', 'cuong', [1, '1', 'cuong'] )
# tuple như list: chứa được hết mọi thứ, những thứ hơn cả string (sau này học)
a, b, c, d, e = our_tuple
print(a) 
print(b)
print(c)
print(d)
print(e)

# Chữa bài 12.12.2021 >>> print(a, b, c, d, e, f) cho nó nhanh nha. 
'''
TÌM HIỂU THÊM VỀ UNPACK TRONG LIST VÀ TUPLE: 
#https://dblog24h.com/python/unpack-tuple-va-list-trong-python-24/

name, age, _, phone = ['Duy', 35, 'Freelancer', '192399443']
print(name)  # Duy
print(age)  # 35
print(phone)  # 192399443

first, *rest = [1, 2, 3, 4]
print(first)  # 1
print(rest)  # [2,3,4]

name, *_, phone = ['Trang', 26, 'Chef', '12434344']
print(name)  # Trang
print(phone)  # 12434344
'''

'''
#CÁCH INPUT TUPLE TỪ USER. 
#https://freetuts.net/ep-kieu-du-lieu-trong-python-1702.html

n = int(input('Enter the number of elements of inputed tuple = '))
inputed_list = []  # tuple như list nhưng không thể thay đổi khi đã khai báo.
for i in range(n): 
    inputed_list.append(input("Enter each element: "))  #Giống list: Nhét cái gì vào cũng được. 
inputed_tuple = tuple(inputed_list)    # chuyển từ list đã khai báo thành tuple. 
print(inputed_tuple)        #("[1, 'cuong']", "(1, 'cuong')")
print(type(inputed_tuple))     #<class 'tuple'>, và các elements trong tuple này đều ở dạng string, chú ý chuyển đổi nếu cần dùng. 

# Vậy có cách nào để khi mà mình input vào (1, 'cuong') hoặc [] thì tự động nhận dạng và chuyển thành kiều list, tuple được không?
# Câu trả lời có thể là không, nên đành giữ các elements của tuple ở dạng string hết. Khi cần thì có thể chuyển dạng. 
# (Giống như input 1 list thì các elements cũng đều ở string hết.)

our_tuple = 1, "[1, '1', 'cuong']", [1, '1', 'cuong']
print(our_tuple[1]) # [1, '1', 'cuong']
# print(type(our_tuple[1]))   # <class 'str'>
print(our_tuple[2])   #[1, '1', 'cuong']
# print(type(our_tuple[2]))  # <class 'list'>
# output nhìn giống nhau, nhưng kiểu dữ liệu thì khác nhau. 
'''