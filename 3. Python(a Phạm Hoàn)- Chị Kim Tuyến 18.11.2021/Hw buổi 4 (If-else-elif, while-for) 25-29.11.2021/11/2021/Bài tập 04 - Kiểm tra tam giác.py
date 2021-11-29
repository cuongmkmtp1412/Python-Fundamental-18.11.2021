'''
Bài 04. Lập trình thực hiện các công việc sau:
    1. Nhập 3 số a, b, c bất kì
    2. Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    3. Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
'''
a, b, c = float(input("Enter cạnh a = ")), float(input("Enter cạnh b = ")), float(input("Enter cạnh c = ")), 
if a + b + c  <= 2 * max (a, b, c) : 
    print(f"{a}, {b}, {c} không là độ dài 3 cạnh của một tam giác.")
else: 
    print(f"{a}, {b}, {c} là độ dài 3 cạnh của một tam giác.")
    if a**2 + b**2 + c**2 == 2 * max(a, b, c) **2: 
        print(f"Và tam giác tạo thành là tam giác vuông, với cạnh huyền = {max(a, b, c)}")
    else: 
        print("Và tam giác tạo thành không là tam giác vuông.")