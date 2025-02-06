list_1 = [1,888,'h',44,['g',1,3]]
if len(list_1) == 0:
    print(list_1)
else:
    print([list_1[:len(list_1) // 2 + len(list_1) % 2], list_1[len(list_1) // 2 + len(list_1) % 2:]])
# якщо к-ть елементів парна, то ділить навпіл, бо len(list_1)%2 = 0
# якщо ж к-ть елементів непарна, то додає 1, бо len(list_1)%2 = 1