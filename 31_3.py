try:
    a,b = map(float, input("Введіть два числа через пробіл: ").split())
    operation = input('Введіть дію: ').strip()
    results = {"+": a + b, "-": a - b, "*": a * b, "/": (a / b) if b != 0 else "Невизначеність"}
    print(f'{a} {operation} {b if b >= 0 else f"({b})"} = {results[operation]}')
except ValueError:
    print("Помилка: не введено коректно 2 числа")
except KeyError:
    print("Помилка: неправильна операція")