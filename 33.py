lst = [1, 888, 'h', 44, 33]
# якщо к-ть елементів парна, то ділить навпіл, бо len(list_1)%2 = 0, інакше len(list_1)%2 = 1 і ділить з першою більшою к-тю елементів
print(lst if not lst else [lst[:len(lst) // 2 + len(lst) % 2], lst[len(lst) // 2 + len(lst) % 2:]])
