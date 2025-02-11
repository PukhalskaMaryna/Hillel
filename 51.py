import string
import keyword
my_variable = input("введіть ім'я змінної: ")
print(
    not any((i.isupper() or i in string.punctuation.replace("_", " ") for i in my_variable)) # перебір елементів рядка і перевірка на велику літеру або чи входить в список символів
    and not (my_variable in keyword.kwlist) # не входить в список зарезервованих
    and not (my_variable[0].isdigit()) # 1 символ не є числом
    and (my_variable.count("_") != len(my_variable) if len(my_variable) > 1 else all(""))   # рахує к-ть _
    )




