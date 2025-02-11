except_key = "y"
while except_key.lower().strip() == "y":
    try:
            a = float(input("Введіть перше число: ").strip())
            b = float(input("Введіть друге число: ").strip())
            results = ["+", a + b, "-", a - b, "*", a * b, "/", a / b if b != 0 else "Невизначеність"]
            operation = input('Введіть дію: ').strip()
            print("Помилка: неправильна дія") if operation not in ("+", "-", "*", "/") else print(f'{a} {operation} {b if b >= 0 else f"({b})"} = {results[results.index(operation) + 1]}')
    except ValueError:
        print("Помилка: не коректне число")
    except_key = input("Для продовження введіть Y: ")