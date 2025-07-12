# 1. Рядки (Strings):
# Напишіть функцію, яка приймає рядок і повертає його довжину.
def get_str_len(my_str: str) -> int:
    return len(my_str)
# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
def get_concat_str(my_str: str, my_str2: str) -> str:
    return my_str + my_str2

# 2. Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає й -> int:ого квадрат.
def get_sq(num):
    return num ** 2
# Створіть функцію, яка приймає два числа і повертає їхню суму.
def get_sum(num,num2):
    return num + num2
# Створіть функцію яка приймає 2 числа типу int,
# виконує операцію ділення та повертає цілу частину і залишок
def get_div(num: int,num2: int) -> tuple:
    return num // num2, num % num2

# 3. Списки (Lists):
# Напишіть функцію для обчислення середнього значення списку чисел.
def get_average(my_list: list) -> float:
    return sum(my_list) / len(my_list) if my_list else 0
# Реалізуйте функцію, яка приймає два списки і повертає список,
# який містить спільні елементи обох списків.
def get_uniq_list(my_list: list, my_list2: list) -> list:
    return list(set(my_list) & set(my_list2))

# 4. Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
def get_keys(my_dict: dict) -> list:
    return list(my_dict.keys())
# Реалізуйте функцію, яка приймає два словники і повертає новий словник,
# який є об'єднанням обох словників
def get_uniq_dict(my_dict: dict, my_dict2: dict) -> dict:
    return {**my_dict, **my_dict2}

# 5. Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
def get_union_set(my_set: set, my_set2: set) -> set:
    return my_set | my_set2
# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
def check_subset(my_set: set, my_set2: set) -> bool:
    return my_set.issubset(my_set2)

# 6. Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне",
# якщо число парне, і "Непарне", якщо непарне.
def check_even(num: int) -> str:
    return "Парне" if num % 2 == 0 else "Непарне"
# Створіть функцію, яка приймає список чисел і повертає новий список,
# що містить тільки парні числа.
def get_even_list(my_list: list) -> list:
    result_list = [i for i in my_list if i % 2 == 0]
    return result_list

