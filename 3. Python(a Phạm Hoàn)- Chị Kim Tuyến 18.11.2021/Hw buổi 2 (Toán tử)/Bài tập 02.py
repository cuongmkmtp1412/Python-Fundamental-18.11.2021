'''Bài 02. Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>
'''
x, y, z= float(input("Enter float a")), float(input("Enter float b")), float(input("float c")) # giữa các số nên có khoảng trắng
import math
F= (x+y+z)/(x**2+y**2+1) - abs(x-z*math.cos(y))     # ban đầu ghi là (x^2+y^2+1) và hiện lỗi: TypeError: unsupported operand type(s) for ^: 'float' and 'float'
print(f"Gia tri cua F = {F}") # Nhúng biến F vào trong string
