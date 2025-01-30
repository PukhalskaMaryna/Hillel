# якщо згадаєте, можете, будь ласка, на наступному уроці показати як робити масову заміну,
# наприклад по всьому коду замінити щось на щось
# і чи є якісь "гарячі" клавіші, якими зручно користуватись
# дуже не сваріть, трішки погуглила і нагуглила .isnumeric()
num_1 = input('введіть перше число: ')
num_2 = input('введіть друге число: ')
operation = input('введіть дію: ')

if  num_1.isnumeric() and num_2.isnumeric(): # перевірка на те, чи є числами
    num_1 = int(num_1)
    num_2 = int(num_2)
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
    print('введіть САМЕ!! числа')