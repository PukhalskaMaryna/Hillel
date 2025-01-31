try:
    a = float(input('Введіть перше число: '))
    b = float(input('Введіть друге число: '))
    operation = input('Введіть дію: ').strip()
    results = {"+": a + b, "-": a - b, "*": a * b, "/": (a / b) if b != 0 else None}
    print(f'{a} {operation} {b if b >= 0 else f"({b})"} = {results[operation]}')
except Exception as e:
    print(e)