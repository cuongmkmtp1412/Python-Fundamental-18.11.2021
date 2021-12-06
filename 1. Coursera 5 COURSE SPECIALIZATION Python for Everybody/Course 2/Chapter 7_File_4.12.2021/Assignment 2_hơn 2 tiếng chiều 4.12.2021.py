'''
7.2 Reads through the file, looking for lines of the form:
                X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.

Desired Output
    Average spam confidence: 0.7507185185185187
'''

# Tìm cách để tách số thập phân khỏi string.  (gg))
# Khó khăn nhất, còn tính avarage not use sum is easy

# cách 1: dùng re
'''
#https://www.tutorialspoint.com/python/python_reg_expressions.htm
#https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/thao-tac-voi-chuoi-string-trong-python/tach-so-trong-chuoi-python/
import re    #help(re)   # hoặc giữ Ctrl và kích chuột trái vào <re>
phone = "2004.959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*', "", phone)
print ("Phone Num : ", num)       # Phone Num :  2004.959-559

# mất # thì số ko hiện 
# mất . hoặc * thì ko bỏ được chữ đằng sau 
# mất $ ở <r'#.*$'> thì chả sao cả 

# Cú pháp re.sub ( r'\D' , '', str)  help(re.sub)

# Remove anything other than digits

num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)        # Phone Num :  2004959559

# Cố gắng đọc và suy nghĩ rất nhiều để dùng modulo re nhưng ko thành công. 
Rốt cuộc phải thay <\D> thành kí tự gì để lấy được 0.8475 đây/ 
'''

#Đến tối thì Cách 1 được hoàn thành (nhờ sự gợi ý của anh Phạm Quan Hà cho 3/5 dòng). 
'''
import re
str_input = 'X-DSPAM-Confidence:      19.8475'
list_num = re.findall(r'\d+', str_input)    # ['19', '8475']
str_num = list_num[0]+ '.' + list_num[1]    # '19.8475'
number= float(str_num)  
# Ơ nhưng nếu có nhiều số thập phân hơn thì ko tách kiểu này được.
# ví dụ: fasjogjd 2021, 12.2335, 10.154 
'''

#Cách 2: anh Phạm Hoàn gợi ý dùng split string và mình triển. 
'''
str_input = "X-DSPAM-Confidence:    0.8475"

list_input = str_input.split(' ')   #  ['X-DSPAM-Confidence:', '', '', '', '0.8475']
for i in list_input:
    try:
        i = float(i)
    except: 
        continue
    print(i)
#Tách thử cái này ? 'Cho một đống số:10.256,16.356,13.265' 
(Giả sử người nhập làm ẩu ko để khoảng trắng ở giữa.)
 
'''

###Đây là bài nộp 


# Use the file name mbox-short.txt as the file name
#bài ngắn thì ko cần cmt. Dài thì đương nhiên cần. 
fname = input("Enter file name: ")
file_handle = open(fname)
 
sun_input = 0      #đề bài ko cho dùng hàm sum để tính tổng và ko đặt tên biến là sum. 
count = 0

for line in file_handle:    #check từng line
    if line.startswith("X-DSPAM-Confidence:"):      # if 3 < 5 (not is True/ False)
        list_line = line.split(' ')      #tách chuỗi bởi các khoảng trắng, để tạo thành list. 
        for number in list_line:
            try:
                number = float(number)  # Tách lấy float. 
            except: 
                continue                # ko phải float thì tiếp tục vòng lặp
            sun_input += float(number)
            count +=1
avarage = sun_input/count  
print(f'Average spam confidence: {avarage}')  
# Desired Output
    #Average spam confidence: 0.7507185185185187
    