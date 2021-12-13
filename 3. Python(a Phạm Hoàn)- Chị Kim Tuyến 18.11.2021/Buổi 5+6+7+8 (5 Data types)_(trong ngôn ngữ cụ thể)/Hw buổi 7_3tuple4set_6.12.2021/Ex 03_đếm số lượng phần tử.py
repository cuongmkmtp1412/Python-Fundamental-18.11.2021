#Đoàn Ngọc Cường
'''
Bài 03: Cho một list chứa nhiều phần tử mang nhiều kiểu dữ liệu khác nhau,
,trong đó có một phần tử kiểu tuple.
Viết chương trình đếm số lượng các phần tử trong một list đó, 
đến khi gặp một phần tử kiểu tuple.
'''

inputed_list = [1, '1', 'cuong', (1, '1', 'cuong', [1, '1', 'cuong'] ), [1, '1', 'cuong']]
for i in range(len(inputed_list)): #duyệt tuple có 2 cách như list và string.
    if type(inputed_list[i]) is tuple:  # ban đầu ngu như này <if type(i) is tuple: > 
        print(f'Số lượng các phần tử trong list đó, đến khi gặp một phần tử kiểu tuple là: {i+1}', end = '.')
        # end = '. ' kết thúc là dấu chấm và cách ra (ko hiện space), thay vì \n
        print(f'Tức là tuple con đầu tiên trong list ban đầu là phần tử thứ {i+1}')
        quit()

