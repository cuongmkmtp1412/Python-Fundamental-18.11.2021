#Đoàn Ngọc Cường-
'''
https://classroom.google.com/u/0/c/NDM1NTgzOTIwODcx/a/NDQxMzk2MTIyMDUw/details
Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 
(Gợi ý: dùng list chứa list).
'''
# Nhập ma trận vuông cấp 3: 
'''
https://quantrimang.com/ma-tran-trong-python-160014
Ma trận trong Python sử dụng nested list and thư viện NumPy.
'''
import numpy as np

# Nhập matrix A
support_H1A = []               
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H1A.append(int(_input)) 

support_H2A = []       # Nhập vào các giá trị ở hàng 2      
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H2A.append(int(_input)) 
    
support_H3A = []  #>>> Các giá trị ở Hàng 3
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H3A.append(int(_input)) 

<<<<<<< HEAD
=======
A = []
A.extend([support_H1A, support_H2A, support_H3A])   # >>> A [[], [], []]

# Nhập matrix B: 
support_H1B = []               
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H1B.append(int(_input)) 

support_H2B = []       # Nhập vào các giá trị ở hàng 2      
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H2B.append(int(_input)) 
    
support_H3B = []  #>>> Các giá trị ở Hàng 3
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H3B.append(int(_input)) 

B = []
B.extend([support_H1B, support_H2B, support_H3B])   # >>> B [[], [], []]

# Chắc chắn sẽ cải tiến để việc nhập ma trận đơn giản hơn, các hàm gọn hơn.  

# Tính nhân ma trận    (Có thể dùng for nhiều vòng lặp)
A = np.array(A)    #A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array(B)    #B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C = A.dot(B)      
print(f'Tích của 2 ma trận đã nhập là: {C}')

# Kết thúc bài tập về nhà cuối cùng hôm nay: Liên tục từ 12 h trưa đến 21h 40 phút tối 6.12.2021
# 9 tiếng code miệt mài, :V #Đoàn Ngọc Cường-
'''
Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 
(Gợi ý: dùng list chứa list).
'''
# Nhập ma trận vuông cấp 3: 
'''
https://quantrimang.com/ma-tran-trong-python-160014
Ma trận trong Python sử dụng nested list and thư viện NumPy.
'''
import numpy as np

# Nhập matrix A
support_H1A = []               
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H1A.append(int(_input)) 

support_H2A = []       # Nhập vào các giá trị ở hàng 2      
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H2A.append(int(_input)) 
    
support_H3A = []  #>>> Các giá trị ở Hàng 3
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H3A.append(int(_input)) 

>>>>>>> 1ae64e1416a48ce7c342fdd5c5b99e25beea1635
A = []
A.extend([support_H1A, support_H2A, support_H3A])   # >>> A [[], [], []]

# Nhập matrix B: 
support_H1B = []               
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H1B.append(int(_input)) 

support_H2B = []       # Nhập vào các giá trị ở hàng 2      
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H2B.append(int(_input)) 
    
support_H3B = []  #>>> Các giá trị ở Hàng 3
for i in range(0, 3):      
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_H3B.append(int(_input)) 

B = []
B.extend([support_H1B, support_H2B, support_H3B])   # >>> B [[], [], []]
<<<<<<< HEAD

# Chắc chắn sẽ cải tiến để việc nhập ma trận đơn giản hơn, các hàm gọn hơn.  

=======

# Chắc chắn sẽ cải tiến để việc nhập ma trận đơn giản hơn, các hàm gọn hơn.  

>>>>>>> 1ae64e1416a48ce7c342fdd5c5b99e25beea1635
# Tính nhân ma trận    (Có thể dùng for nhiều vòng lặp)
A = np.array(A)    #A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array(B)    #B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C = A.dot(B)      
print(f'Tích của 2 ma trận đã nhập là: {C}')
<<<<<<< HEAD

# Kết thúc bài tập về nhà cuối cùng hôm nay: Liên tục từ 12 h trưa đến 21h 40 phút tối 6.12.2021
# 9 tiếng code miệt mài, :V 
'''
Nhận xét a Phạm Hoàn 8.12.2021
1 nhận xét riêng tư

Epsilon Bit6 thg 12
good job ;)

'''
=======

# Kết thúc bài tập về nhà cuối cùng hôm nay: Liên tục từ 12 h trưa đến 21h 40 phút tối 6.12.2021
# 9 tiếng code miệt mài, :V 
>>>>>>> 1ae64e1416a48ce7c342fdd5c5b99e25beea1635
