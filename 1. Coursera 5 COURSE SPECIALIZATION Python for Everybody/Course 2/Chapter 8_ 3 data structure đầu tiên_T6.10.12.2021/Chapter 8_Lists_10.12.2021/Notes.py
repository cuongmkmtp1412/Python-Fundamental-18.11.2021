# Mình đã học về lists lần đầu tiên từ hôm trước 14/11/2021 - trong khoá của codelearn.io
# Học lần thứ 2 là: T5/2/12/2021- khi học a Phạm Hoàn. 
# help(dir)  #dir([object]) -> list of strings
# print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
x = list()   #hoặc x = []    # tạo list rỗng. 
x = list(range(5))  #>>> print(x) >>>[0, 1, 2, 3, 4] (A list of integers) # Học tới lần thứ 3 mới biết cái này. 
'''Built-in function() and lists : max() , min(), sum(), len(), 
Function() là những hàm được xây dựng chung, còn method() riêng cho các objects. 
'''

# Double Split Pattern: 
line = "From cuongmkmtpgoldfinch@gmail.com Fri Dec 10 10:01:50 2021" 
words = line.split()   # mặc định là .split(" ")
email = words[1]
pieces = email.split('@')
print(pieces[1])  

'''
Question 1
How are "collection" variables different from normal variables?   (1 point)
Collection variables can only store a single value
Collection variables can store multiple values in a single variable   <me chọn>
Collection variables merge streams of output into a single stream
Collection variables pull multiple network documents together
'''
