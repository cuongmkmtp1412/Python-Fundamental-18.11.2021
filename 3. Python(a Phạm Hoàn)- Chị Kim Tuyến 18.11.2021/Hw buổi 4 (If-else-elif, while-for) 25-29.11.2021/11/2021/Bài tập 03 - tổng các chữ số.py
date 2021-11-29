'''Bài 03. Lập chương trình thực hiện các công việc sau:
    1. Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    2. Tính tổng các chữ số của số đó.
    3. Hiển thị kết qủa ra màn hình'''
n = input("Nhập số nguyên dương n < 1000 ")
try:                                          #https://pythonbasics.org/try-except/#Built-in-exceptions
    n = int(n)  
except: 
    print("Dữ liệu đầu vào không đúng yêu cầu. Enter again.")   
    quit()
if n >= 1000 or n < 1 : 
    print("Hãy nhập số nguyên dương < 1000. Enter again.")
else: 
    tong_chu_so = 0
    while n > 0: 
        tong_chu_so += n % 10
        n = int(n/10)
    print(f'tổng các chữ số của số n đã nhập là = {tong_chu_so}')

# Có cách nào dùng try- except để kiểm soát 1<= n < 1000 mà ko cần dùng thay cho if-else được ko ?
# xử lý Value Error > https://www.journaldev.com/33500/python-valueerror-exception-handling-examples


