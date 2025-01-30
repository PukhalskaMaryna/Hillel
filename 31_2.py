# якщо згадаєте, можете, будь ласка, на наступному уроці показати як робити масову заміну,
# наприклад по всьому коду замінити щось на щось
# і чи є якісь "гарячі" клавіші, якими зручно користуватись
# не сваріться сильно, бо пішла гуглити обробник помилок, так як isdigit() не захоплює від'ємні числа
num_1 = input('введіть перше число: ')
num_2 = input('введіть друге число: ')
test_for_num_1 = True
test_for_num_2 = True
operation = input('введіть дію: ')

try:
     num_1 = float(num_1)
except ValueError:
     test_for_num_1 = False

try:
     num_2 = float(num_2)
except ValueError:
     test_for_num_2 = False

# перевірка на те, чи є числами, чи правильна дія
if  test_for_num_1 and test_for_num_2 and (operation == '+' or operation == '-' or operation == '*' or operation == '/'):

    #num_1 = int(num_1)
    #num_2 = int(num_2)
    if num_2 >= 0: # перевірка на знак 2-го числа, щоб красиво прописати дію: з дужками або без
        if operation == '+':
            print(num_1,'+',num_2,'=',num_1+num_2)
        elif operation == '-':
            print(num_1,'-',num_2,'=',num_1-num_2)
        elif operation == "*":
            print(num_1,'*',num_2,'=',num_1*num_2)
        elif operation == '/':
            if num_2 == 0:
                print('не можна ділити на 0!!!')
            else:
                print(num_1,'/',num_2,'=',num_1 / num_2)
    else:
        if operation == '+':
            print(num_1,'+ (',num_2,') =',num_1+num_2)
        elif operation == '-':
                print(num_1,'- (',num_2,') =',num_1-num_2)
        elif operation == '*':
            print(num_1,'* (',num_2,') =',num_1*num_2)
        elif operation == '/': # перевірка 2-го числа на 0 не потрібна, бо у нас вище точно відомо, що друге число від'ємне
            print(num_1,'/',num_2,') =',num_1/num_2)
else:
    if  not (test_for_num_1 and test_for_num_2):
        print('помилка: ви ввели не число')
    else:
        print('помилка: ви ввели невірну дію')