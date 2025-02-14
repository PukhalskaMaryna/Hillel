import string
from num2words import num2words
# словничок відповідностей: назва числа - число
dic ={num2words(i):str(i) for i in range(1,10)}

with open('C:/Users/puhal/Desktop/adventofcode/1_2.txt', 'r') as file:
    content = tuple(file.read().splitlines())
print(content)
content = ("two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen")
# заміна всіх назв чисел на числа
for k,v in dic.items():
    content = tuple(i.replace(k,v) for i in content)
print(content)
content = tuple(
    # цикл наповнення кортежу рядками з 1 і останньої цифри або подвоєння цифри, якщо вона 1 в рядку
    i[0] + i[-1] for i in (
        # цикл перенаповнення кортежу content з чисткою букв по краях
        i.strip(string.ascii_letters) for i in content
    )
)
print(content)
print(sum(int(i) for i in content))
# 54632
