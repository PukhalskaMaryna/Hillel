except_key = "y"
while except_key.lower().strip() == "y":
    try:
            a = [float(input("Введіть перше число: ").strip()),float(input("Введіть друге число: ").strip()),input('Введіть дію: ').strip()]
            results = ["+", a[0] + a[1], "-", a[0] - a[1], "*", a[0] * a[1], "/", a[0] / a[1] if a[1] != 0 else "Невизначеність"]
            print("Помилка: неправильна дія") if a[2] not in ("+", "-", "*", "/") else print(f'{a[0]} {a[2]} {a[1] if a[1] >= 0 else f"({a[1]})"} = {results[results.index(a[2]) + 1]}')
    except ValueError:
        print("Помилка: не коректне число")
    except_key = input("Для продовження введіть Y: ")