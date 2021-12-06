from numpy.lib.function_base import append

   
support_A = []              
for i in range(0, 3*3): 
    _input = input("Nhập matrix từ phải sang trái, từ trên xuống dưới: ")          
    support_A.append(_input)
for i in support_A[0:3]:
    support_A.append(int(i))
print(support_A)

