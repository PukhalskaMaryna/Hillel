import string

with open('C:/Users/puhal/Desktop/adventofcode/1.txt', 'r') as file:
    content = (
        # цикл наповнення кортежу рядками з 1 і останньої цифри або подвоєння цифри, якщо вона 1 в рядку
        i[0] + i[-1] for i in (
            # цикл наповнення кортежу рядками файлу 1.txt в окремі елементи з чисткою букв по краях
            i.strip(string.ascii_letters) for i in file.read().splitlines()
        )
    )

print(sum(int(i) for i in content))
# 54632
