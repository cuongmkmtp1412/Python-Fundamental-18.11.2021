# Đoàn Ngọc Cường 
'''
Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
'''

a_sentence = input("Enter a sentence: ")  # Dùng comment khi test code để ko cần input() nhiều lần. 
# a_sentence = 'Một cộng một sẽ hơn hai. Vì một cuộc sống, không có đau thương chỉ có tiếng cười vui!'
# Tạm xét trường hợp có (.) và (,) , các trường hợp khác sẽ tốn code hơn. 
string_words_list = a_sentence.split(" ")   # list chứa các từ và có từ chứa dấu , . 

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


