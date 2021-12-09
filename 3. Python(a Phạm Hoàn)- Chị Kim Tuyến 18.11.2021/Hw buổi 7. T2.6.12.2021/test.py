k = int(input("So phan tu cua list: "))
list1 = []
for i in range(k):
    n = int(input(f"So phan tu con cua tuple[{i}]: "))
    tuple1 = tuple([int(input(f"tuple[{i}][{j}] = ")) for j in range(n)])
    list1.append(tuple1)
print(list1)
list2 = []
for i in range(k):
    n = max(list[i][1] for i in range(k))
    list2.append(n)
print(list2)