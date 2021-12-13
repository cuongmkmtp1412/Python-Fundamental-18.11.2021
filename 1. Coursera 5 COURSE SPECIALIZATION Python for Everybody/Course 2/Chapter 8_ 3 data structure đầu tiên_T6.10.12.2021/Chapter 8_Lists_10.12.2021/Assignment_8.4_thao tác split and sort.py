# ban đầu để tên file / ??? mà thụt lề chỉ có 3 rất điêu. https://qastack.vn/programming/34174207/how-to-change-indentation-in-visual-studio-code
'''
8.4 Open the file romeo.txt and read it line by line.
 For each line, split the line into a list of words using the split() method.
  The program should build a list of words
  . For each word on each line check to see if the word is already in the list 
  and if not append it to the list. When the program completes,
   sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''
# Đoàn Ngọc Cường_ tối t6 10/12/2021.   (Due_T2/13/12/2021)
# Build a list of words, (ko có 2 từ giống nhau), sort rồi print ra. 

fname = input("Enter file name: ")   # Enter file name
file_handle = open(fname)                     #file handle: xử lý tập tin
output_list = list()                  # lst = []
for line in file_handle:               # duyệt từng dòng của fh
   # line = line.rstrip()        # thao tác xoá các khoảng trắng bên phải của line   (right_strip)
    list_word_line = line.split()      # STRING, TUPLE KHÔNG THỂ THAY ĐỔI KHI ĐÃ KHAI BÁO, NÊN TA GÁN NÓ VÀO MỘT CÁI BIẾN KHÁC
    # list_word_line chứa các từ trong một dòng
    for word in list_word_line: 
        if word not in output_list: 
            output_list.append(word)    

# print(sp_list) 
output_list.sort()     #obj.sort() method thay đổi trực tiếp list : Ban đầu mình code như này:  output_list = sp_list.sort() thì print(output_list) ra None
# output_list = sorted(output_list)            # and sorted() function
print(output_list)

        