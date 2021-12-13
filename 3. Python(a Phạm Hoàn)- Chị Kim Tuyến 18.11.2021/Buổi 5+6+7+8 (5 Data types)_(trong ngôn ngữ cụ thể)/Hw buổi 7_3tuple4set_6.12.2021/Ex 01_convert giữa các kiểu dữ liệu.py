#Đoàn Ngọc Cường 

'''
Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
'''
our_tuple = 1, '1', 'cuong', [1, '1', 'cuong'], (1, '1', 'cuong', [1, '1', 'cuong'] )
converted_list = list(our_tuple)  # chuyển tuple sang list.
print(type(converted_list))
converted_tuple = tuple(converted_list)   # chuyển list sang tuple.
print(type(converted_tuple))