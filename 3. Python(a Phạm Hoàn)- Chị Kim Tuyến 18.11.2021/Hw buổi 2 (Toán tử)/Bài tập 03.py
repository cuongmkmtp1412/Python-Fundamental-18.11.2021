'''Bài 03. Hãy viết đoạn chương trình thực hiện các việc sau:
    1. Nhập hai số nguyên a và b từ bàn phím
    2. Thực hiện phép chia lấy nguyên (//) và chia lấy dư (%) của a cho b
    3. In kết quả 2 phép chia ra màn hình
Lưu ý: Khi nhập giá trị để test, cần thực hiện các trường hợp sau và xem kết quả thu được
    - TH1: a > 0, b < 0
    - TH2: a < 0, b > 0
    - TH3: a < 0, b < 0   '''
a, b= int(input("Enter int a")), int(input("Enter int b"))
print(a//b)
print(a%b)
