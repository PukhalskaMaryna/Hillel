import string
import keyword
my_txt = input("введіть текст: ")
print(not any((i.isupper() or i in string.punctuation.replace("_", " ") for i in my_txt)) # перебір елементів рядка і перевірка на велику літеру або чи входить в список символів
and not (my_txt in keyword.kwlist) # не входить в список зарезервованих
and not (my_txt[0].isdigit()) # 1 символ не є числом
and my_txt.count("_") < 2 # рахує к-ть _
)




