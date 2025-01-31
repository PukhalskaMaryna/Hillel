#ver_1
l_1 = [10,12,3,4]
l_1.insert(0, l_1[-1])
l_1.pop()
print(l_1)

#ver_2
l_2 = [10,12,3,4]
print([l_2[-1]]+l_2[0:len(l_2)-1])
