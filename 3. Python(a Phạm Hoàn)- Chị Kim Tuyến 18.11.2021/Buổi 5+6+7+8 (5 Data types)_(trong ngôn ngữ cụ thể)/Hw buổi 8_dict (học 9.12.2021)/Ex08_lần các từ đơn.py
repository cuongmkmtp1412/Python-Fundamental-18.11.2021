# Đoàn Ngọc Cường: 13.12.2021
'''
Bài 08: Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
(Nâng cấp từ Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một String)
'''

# Bước 1: bỏ đi các dấu chám, dáu phẩy. (dùng bài 11 hw buổi trước (buổi 7- tuple, set))
# a_paragraph = input("Enter a sentence: ") 
a_paragraph = 'Một cộng một bằng hai, hai cộng hai bằng bốn, bốn cộng bốn bằng tám.'
string_words_list = a_paragraph.split(" ")   # list chứa cả các từ và có từ chứa dấu , . 

best_words_list = []       # list loại bỏ dấu , . ? !
for word in string_words_list:
    if "." in  word or "," in word or "!" in word or "?" in word: # tạm bỏ qua các kí tự khác.
        best_words_list.append(word[:len(word)-1])  # Bỏ đi phần tử cuối cùng rồi ghép vào list best
    else: 
        best_words_list.append(word)
print(best_words_list)

# Bước 2: đếm số lần xuất hiện của từ và in ra dạng dict. (dùng bài 7 vừa làm buổi 8 này.)
output = {}
for i in best_words_list: 
    output[i] = best_words_list.count(i)
print(output)



'''
# Đoàn Ngọc Cường 
Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.

a_sentence = input("Enter a sentence: ")  # Dùng comment khi test code để ko cần input() nhiều lần. 
# a_sentence = 'Một cộng một sẽ hơn hai. Vì một cuộc sống, không có đau thương chỉ có tiếng cười vui!'
# Tạm xét trường hợp có (.) và (,) , các trường hợp khác sẽ tốn code hơn. 
string_words_list = a_.split(" ")   # list chứa các từ và có từ chứa dấu , . 

best_words_list, long_best_words_list = [], []

for word in string_words_list:
    if "." in  word or "," in word or "!" in word or "?" in word: # tạm bỏ qua các kí tự khác.
        best_words_list.append(word[:len(word)-1])  # Bỏ đi phần tử cuối cùng rồi ghép vào list best
        long_best_words_list.append(len(word[:len(word)-1]))   # Thêm len của phần tử đó vào list để lát so sánh và tìm từ có độ dài max 
    else: 
        best_words_list.append(word)
        long_best_words_list.append(len(word))
print(best_words_list)

# Ban đầu dùng: longest_word = max(best_words_list)    >>> print ra từ lớn nhất theo bảng... Chứ không phải độ dài max
print(max(long_best_words_list))  # Tìm ra được độ dài max của một từ

print("(Các) từ dài nhất trong một câu vừa nhập vào từ bàn phím là: ", end = "") # print trước một câu này, nhưng ko xuống dòng. 

for i in best_words_list:   # quay trở lại duyệt best_words_list 
    if len(i) == max(long_best_words_list): # Nếu i có độ dài bằng = max thì 
        print(i, end = ",")
print()   # để tránh output gần với PS C (chỉ mục)


'''