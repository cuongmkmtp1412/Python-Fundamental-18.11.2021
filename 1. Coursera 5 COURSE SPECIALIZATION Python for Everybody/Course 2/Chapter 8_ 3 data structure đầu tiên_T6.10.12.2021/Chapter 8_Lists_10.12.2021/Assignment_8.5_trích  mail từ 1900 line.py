# Đoàn Ngọc Cường 23 h tối 10/12/2021:
# Lại gặp lỗi như tối qua: Assignment_8.5_tr├¡ch xuß║Ñt mail ng╞░ß╗¥i gß╗¡i tß╗½ 1900 line_txt.py': [Errno 2] No such file or directory
# (Vì đặt tên tệp quá dài)
'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''
# Trích xuất mail người dùng ở các dòng start with "From" not "From:" print ra và count. 
# (nhiệm vụ count là phụ thôi)
# fname = input("Enter file name: ")
# fh = open(fname)        #fh : file handle: xử lý tệp

fh = open('mbox-short.txt')    # để khi test đỡ phải input nhiều

output_list = []    # list()
for line in fh: 
    if line.startswith("From") and line.startswith("From:") is False:
        list_word_line = line.split()    # line này là string nên split() phải gán vào một biến mới 
        # Bỏ qua bước line.rstrip()
        output_list.append(list_word_line[1])     # thêm phần tử index 1- tức là mail vào list output. 
# lúc này output_list đã chứa hết các mail cần print rồi
for mail in output_list: 
    print(mail)
print(f"There were", len(output_list), "lines in the file with From as the first word")
# Ban đầu viết là {len(output_list)}  là ngu vì nhúng biến thôi, trong khi len() là một số rồi. 
# Làm chắc chắn, comment từng tí một >>> run phát đúng luôn. 

'''
Chữa bài: 
- là khi mà ko dùng start.swith mà dùng line[0] != 'From' thì phải chú ý nếu có thư mục rỗng nó sẽ báo 
<list index out of range>
'''
for line in fh: 
    list_word_line = line.split()  # cắt mỗi dòng bởi khoảng trắng thành list các từ (bỏ qua line.rstrip)
    if len(list_word_line) < 1: # trường hợp dòng trống thì list_word_line = [] khi đó sẽ báo lỗi nếu ta cố gắng dùng index
        continue   # bỏ qua trường hợp này và tiếp tục vòng lặp.
    if list_word_line[0] != 'From':   # có thể gộp 2 điều kiện này lại. 
        continue
    print(list_word_line[1])
# Cách này thì ko cần tạo list nhưng cần chú ý đến việc gặp lỗi khi gọi chỉ mục của list rỗng. 
