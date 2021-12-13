'''
Bài 02: Viết chương trình đảo ngược một tuple.
'''

#Cách 1: 
'''
Các phương thức của Tuple - rất ít: 
tuple.count(element) method
tuple.index(element) method : index của phần tử đầu từ trái sang phải.
>>> nên ta sẽ chuyển sang string để xử lý. 
# Đảo ngược list : list.reverse() method, 
'''

# Cách 2: thông minh hơn: tuple giống list nên ta có thể dùng split tuple như với list [i:j:a]. 
our_tuple = 1, '1', 'cuong', [1, '1', 'cuong'], (1, '1', 'cuong', [1, '1', 'cuong'] )
reverse_tuple = our_tuple[::-1]
print(reverse_tuple)
