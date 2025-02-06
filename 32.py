lst = [10,12,'3',4,[1,2,3,4]]
if len(lst) == 0:
    print([])
else:
    lst.insert(0,lst[-1])
    print(lst[:-1])

