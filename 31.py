num_1 = int(input("введіть перше число: "))
num_2 = int(input("введіть друге число: "))
operation = input("введіть дію: ")

if num_2 >= 0: # перевірка на знак 2-ого числа, щоб красиво прописати дію: з дужками або без
    if operation == "+":
        print(num_1,"+",num_2,"=",num_1+num_2)
    elif operation == "-":
            print(num_1,"-",num_2,"=",num_1-num_2)
    elif operation == "*":
        print(num_1,"*",num_2,"=",num_1*num_2)
    elif operation == "/":
        if num_2 == 0:
            print("не можна ділити на 0!!!")
        else:
            print(num_1,"/",num_2,"=",num_1 / num_2)
else:
    if operation == "+":
        print(num_1,"+ (",num_2,") =",num_1+num_2)
    elif operation == "-":
            print(num_1,"- (",num_2,") =",num_1-num_2)
    elif operation == "*":
        print(num_1,"* (",num_2,") =",num_1*num_2)
    elif operation == "/": # перевірка 2-ого числа на 0 не потрібна, бо у нас вище точно відомо, що друге число від'ємне
        print(num_1,"/",num_2,") =",num_1 / num_2)