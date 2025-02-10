import random
lst = [random.randint(1,100) for _ in range(random.randint(3,10))]
print(lst, "==", [lst[0],lst[2],lst[-2]])
