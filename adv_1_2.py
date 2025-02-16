import re # бібліотека регулярок
from num2words import num2words # бібліотека чисел і їх назв
dic ={num2words(i):str(i) for i in range(1,10)} # словничок відповідностей: назва числа - число
dic_reversed ={num2words(i)[::-1]:str(i) for i in range(1,10)} # словничок відповідностей: обернена назва числа - число
pattern = re.compile(rf"{'|'.join(list(dic.keys()))}|\d") # регулярний вираз перебору назв чисел і самих чисел
pattern_reversed = re.compile(rf"{'|'.join(list(dic_reversed.keys()))}|\d") # регулярний вираз перебору обернених назв чисел і самих чисел

with open('C:/Users/puhal/Desktop/adventofcode/1_2.txt', 'r') as file:
    content = tuple(file.read().splitlines())

summ = sum(int(
    # перше число
    (dic.get(pattern.findall(i)[0],pattern.findall(i)[0]))
    +
    # останнє число
    (dic_reversed.get(pattern_reversed.findall(i[::-1])[0],pattern_reversed.findall(i[::-1])[0]))
) for i in content)
print(summ)
#54019
