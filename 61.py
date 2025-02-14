import string

sym_1, sym_2 = map(ord, input("Введіть 2 літери через дефіс: ").replace(' ', '').split("-"))
if sym_1 <= sym_2:
    for c in string.ascii_letters: # цикл для букв, що в одному регістрі
        if ord(c) in range(sym_1, sym_2 + 1):
            print(c, end='')
else:
    for c in string.ascii_letters: # цикл для букв, де перша у нижньому, а друга у верхньому
        if ord(c) in range(sym_1, ord('z') + 1) or ord(c) in range(ord('A'), sym_2 + 1):
            print(c, end='')
