import string

sym_1,sym_2 = map(ord,input("Введіть 2 літери через дефіс: ").replace(' ','').split("-"))
for c in string.ascii_letters:
    if ord(c) in range(sym_1, sym_2+1):
        print(c,end = '')

