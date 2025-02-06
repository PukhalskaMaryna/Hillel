lst = [0, 0, 0, 0, 1, 0, 't', [1, 2, 0], 12, 3]
i = 0 # рахує к-ть 0
while 0 in lst:
    lst.remove(0)
    i += 1
print(lst + [0] * i)
