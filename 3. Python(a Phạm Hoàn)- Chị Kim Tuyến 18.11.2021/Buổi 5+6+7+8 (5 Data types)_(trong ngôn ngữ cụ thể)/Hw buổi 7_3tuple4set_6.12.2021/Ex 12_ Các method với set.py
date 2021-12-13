'''
Bài 12. Viết chương trình để thử lại các phương thức của Set theo danh sách sau
        set.difference_update(other_set)
        set.intersection_update(other_set)
        set.isdisjoint(other_set)
        set.issubset(other_set)
        set.issuperset(other_set)
        set.symmetric_difference_update(other_set)
'''

'''
CHỐT LẠI CÁC METHOD() THAO TÁC VỚI 2 SET
    hơp, giao, bù, bù đối xứng 
    |, &, -, ^
    set_03 = set_01.union(set_02),  intersection, difference, symmetric_difference
    set_01.union_update(set_02) <=> set_01 = set_01.union(set_02) : gán/ update vào set_01, tương tự: ...
'''

'''
# set ko bất biến, nhưng phần tử chứa trong nó phải bất biến.
# set ko sắp thứ tự >> ko truy cập được bằng chỉ mục.  
# ***Các thao tác với 2 tập hợp***
set_01 = {1, 2, 3, 4, (1, 2, 3)}
set_02 = {9, 8, 7, 6, 5, 4}

print(set_01 | set_02)         #Hợp
print(set_01.union(set_02))  
set_01.union.update(set_02)
print(set_01)

print(set_01 & set_02)                # giao của 2 tập
print(set_01.intersection(set_02)) 
set_01.intersection_update(set_02)  
print(set_01)    # set_01 đã bị thay đổi thành giao của 2 set

print(set_01 - set_02)    # phần bù = thuộc A mà ko thuộc B
print(set_01.difference(set_02)) 
set_01.difference_update(set_02)     #method làm thay đổi set ban đầu
print(set_01)   # >>> set_01 đã bị thay đổi thành phần bù của set_01 cho set_02
#>>> _update() : kết quả được cập nhật vào toàn bộ set_01 (set_2 giữ nguyên)

print(set_01 ^ set_02)  #phần bù đối xứng: chứa toàn bộ phần tử của A và B trừ phần chung. 
set_01.symmetric_difference_update(set_02)
print(set_01) 
'''

set.symmetric_difference_update
set_03 = {1, 2, 3}
set_04 = {1,2, 3, 4, 5}
print(set_03.isdisjoint(set_04))    # set.isdisjoint(other_set) return True if two sets are disjoint sets (is-dis-join) - tương tự isnumeric,...

print(set_03.issubset(set_04))    #is tập con
print(set_03.issuperset(set_04))   #is tập mẹ
# set.issubset(other_set)    returns True if all elements of a set are present in another set
# Ngược lại set.issuperset(other_set) method.  
      
      
      

