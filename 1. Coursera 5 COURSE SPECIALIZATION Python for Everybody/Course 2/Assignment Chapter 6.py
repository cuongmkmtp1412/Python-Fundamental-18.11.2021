'''  <https://www.py4e.com/tools/pythonauto/?PHPSESSID=11982ee1b3dcea17fc1010ca5461d4dd>    27.11.2021
6.5 Write code using find() and string slicing (cắt chuỗi) (see section 6.10) to extract 
the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"  >>> 0.8475
'''
text = "X-DSPAM-Confidence:    0.8475"   
find_string=text.find('0.8475')
print(float(text[find_string:find_string+6]))    # text[1:6] thì ko lấy số 6- tương tự for x in range(1,6)
#You should use the float() function to convert from a string to an integer => thêm float