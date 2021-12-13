'''
Chapter 7 Quiz : https://quizlet.com/217754370/py4e-chapter-7-flash-cards/

Question 2: What is stored in a "file handle" that is returned from a successful open() call?
-The handle is a connection to the file's data   >>> Key
-All the data from the file is read into memory and stored in the handle >>> me pick > false

Question 3: What do we use the second parameter of the open() call to indicate?
-How large we expect the file to be
-What disk drive the file is stored on
-Whether we want to read data from the file or write data to the file  => pick 
-The list of folders to be searched to find the file we want to open

Question 5: What is the purpose of the newline character in text files?
-It indicates the end of one line of text and the beginning of another line of text
'''

'''
Assignment 7.1:   https://www.py4e.com/tools/pythonauto/?PHPSESSID=13215ccd5f8bba1d755aeee4080d8b34
7.1 Write a program that prompts for a file name, 
then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt '''

'''

me1: 
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)     ## file handle: xử lý tập tin
for i in fh: 
    i = i.upper()   
    print(i, end="")

>>> output is True but feedback: 
You should use strip() or rstrip() to avoid double newlines. 
You may need to scroll down to see a mis-match of the output.
(I don't see that different from in desired output and my output.)
'''
# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)               # file handle: xử lý tập tin
fh = open('words.txt')

for line in fh: 
    line = line.rstrip()
    for i in line:
        i = i.upper()   #Các method không làm thay đổi str ban đầu,
        print(i, end='')
    print()           # Câu lệnh xuống dòng-mình nghĩ ra trong bài tạo tháp 1\n12\n123\n12\n1

# Sau vài tiếng loay hoay ko thao tác với file được trên vs code, mình đã tìm ra:
#- mở folder chứa file .py và file .txt
#- và chỉ folder đó thôi, ko mở folder mẹ của nó, thì mới thao tác được. 


######### Chữa bài tận đêm 10/12/2021 mới xem: 
for line in fh: 
    line = line.rstrip()
    # for i in line:
    #     i = i.upper()   #Các method không làm thay đổi str ban đầu,
    #     print(i, end='')
    # print()  
    print(line.upper())   # Bài của mình thì upper từng từ một trong dòng. Đây ô thầy upper() cả dòng luôn. Vì bản chất dòng hay từng từ thì cũng là string.     