lst = [0, 1, 7, 2, 4, 8]
summ = 0
for index, element in enumerate(lst):
    if index % 2 == 0:
        summ += element

print(0 if lst == [] else summ * lst[-1])
