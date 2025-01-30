# з надією, що користувач свідомий і введе саме 4 цифри:)

# ver1
# ця версія з циклом мені сподобалась більше
# насправді, ця версія розіб'є не тільки 4 цифрове, але мені було цікаво ввести перевірку і цикл
# синтаксис дуже схожий на sql
a = int(input("введіть 4 цифри: "))
    while a > 0:
        b = 10 ** (len(str(a)) - 1)
        print(a // b)
        a = a % b


# ver2
# максимально примітивна версія без циклу і без перевірки,
a = int(input("введіть 4 цифри: "))
print("результат: ")
print(a // 1000)
print((a % 1000) // 100)
print((a % 100) // 10)
print(a % 10)
