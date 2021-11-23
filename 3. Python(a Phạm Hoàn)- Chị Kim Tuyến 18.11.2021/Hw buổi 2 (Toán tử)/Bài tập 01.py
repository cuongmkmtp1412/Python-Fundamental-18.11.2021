'''
Bài 01. Ngân hàng Vietcombank sẽ cho khách hàng vay tiền nếu họ trên 18 tuổi 
và khoản thu nhập hằng năm tối thiểu 2500$.
Với biến chỉ tuổi của khách là age, biến chỉ thu nhập là income, 
hãy viết biểu thức logic để kiểm tra một khách hàng có được vay vốn hay không?
'''
age= int(input("How old are you?"))
income= float(input("How much is your annual income? ($)"))
if age>18 and income>=2500:
    print("Khách hàng đủ điều kiện vay vồn.")
else: print("Xin lỗi. Bạn chưa đủ điều kiện vay vốn")
# Có cách làm bài này ko dùng if-else không ? 
