'''Yêu cầu người dùng nhập name của họ từ bàn phím.
    2. In ra lời chào với họ đã đến chương trình
    3. Yêu cầu họ nhập năm sinh
    4. Tính toán và in ra số tuổi hiện tại của'''
#author:  Đoàn Ngọc Cường 
user_name= input("What is your name?")
print(f"Hello {user_name}. Welcome to our program")
user_age= input("When were you born?")
try: 
    user_age= int(user_age)
except: 
    print("Enter again.")
    quit()
print(f'Now, your age is {2021-user_age}')
    
