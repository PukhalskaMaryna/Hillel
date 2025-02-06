lst = [0, 0, 0, 1, 0, 't', [1, 2, 0], 12, 3]
lst0 = []
while 0 in lst:
    lst.remove(0)
    lst0 += [0]
print(lst+lst0)
