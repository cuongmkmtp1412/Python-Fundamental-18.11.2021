#Đoàn Ngọc Cường- 9/12/2021
'''
Bài 06: Viết chương trình in ra phần tử thứ 4
 và phần tử thứ 4 từ cuối lên trong một tuple.
'''
our_tuple = 1,[1, '1', 'cuong'], 'cuong', "[1, '1', 'cuong']", (1, '1', 'cuong', [1, '1', 'cuong'] )
if len(our_tuple) < 4: 
    print('Độ dài our_tuple không đủ để thực hiện yêu cầu đề bài')
else: 
    print(f'Phần tử thứ 4 của tuple là: {our_tuple[3]}') # [1, '1', 'cuong']
    #print(type(our_tuple[3]))   # <class 'str'>
    print(f'Phần tử thứ 4 từ cuối lên của tuple là: {our_tuple[-4]} ')   #[1, '1', 'cuong']
    #print(type(our_tuple[-4]))  # <class 'list'>
    # output nhìn giống nhau, nhưng kiểu dữ liệu thì khác nhau. 
