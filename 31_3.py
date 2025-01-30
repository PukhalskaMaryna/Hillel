try:
    a = float(input('Введіть перше число: ').strip())
    b = float(input('Введіть друге число: ').strip())
    operation = input('Введіть дію: ').strip()
    results = {"+": a + b, "-": a - b, "*": a * b, "/": (a / b) if b != 0 else None}
    print(f'{a} {operation} {b if b >= 0 else f"({b})"} = {results[operation]}')
except ValueError:
    print("Введене значення не є числом")
except ZeroDivisionError:
    print("Не можна ділити на нуль")