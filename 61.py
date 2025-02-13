import string

my_str = input("Введіть 2 літери через дефіс: ").replace(' ','')
print(string.ascii_letters[string.ascii_letters.index(my_str[0]):string.ascii_letters.index(my_str[2]) + 1])

