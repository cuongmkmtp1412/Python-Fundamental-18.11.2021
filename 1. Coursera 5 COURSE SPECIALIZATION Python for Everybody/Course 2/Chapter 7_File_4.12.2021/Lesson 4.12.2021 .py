'''
flat - text files: mbox.txt or mboxshort.txt  (mailbox format), not like word or pdf
- making the file avaiable to the code that we are writing 
handle = open(filename, mode), fhand = open('mbox.txt', 'r')
\n represents the Enter button. 

--- So a file handle to the for loop looks like a sequence of lines.
'''

#Example 1: 
fhand = open ('buitra.txt')        
for i in fhand:      #i tương tự như line- từng dòng. 
    print (i) 
# FileNotFoundError: [Errno 2] No such file or directory: 'bui tra.txt'
# khi in sẽ ra thêm một khoảng trắng ở các dòng. 

#Example 2: 
fhand = open('buitra.txt')
for line in fhand:   #khi duyệt line thì tự động xuống dòng rồi. 
    line = line.rstrip()    # để xoá đi khoảng trắng ở bên phải. ko để dòng trống giữa các dòng.
    if line.startswith('From'):
        print(line)   # Thêm một lần xuống dòng nữa. 

# Example 3: 
fname = input("Enter file name: ")
try: 
    fhand = open(fname)   #file handle
except: 
    quit()
for line in fhand: 
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)

#2h sáng 4.12.2021 ('C:>Users>Administrator>Desktop>test>buitra.txt') cũng ko được. xem các video cũng ko thấy hướng dẫn
#Đến chiều khi làm xong assigment 1 thì chợt nảy ra ý tưởng mở folder chứa 2 file .py và .txt .Chứ ko phải mở 2 file riêng rẽ.
# Và chỉ mở folder đó thôi, ko mở folder mẹ to bự fundamental python.  '''