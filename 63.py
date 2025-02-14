import math

numb = int(input("Введіть число: ").replace(" ",""))
while numb > 9:
    numb = math.prod(int(d) for d in str(numb))
print(numb)


