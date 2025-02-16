with open('C:/Users/puhal/Desktop/adventofcode/2.txt', 'r') as file:
    content = {
        # цикл наповнення словника словників
        int(i.split(":")[0].replace("Game ","")):i.split(":")[-1].strip() for i in file.read().splitlines()
    }
print(content)

content = {i: {ii : {iii.strip().split(" ")[-1]:int(iii.strip().split(" ")[0]) for iii in content.get(i).split(";")[ii - 1].strip().split(",")} for ii in range(1,len(content.get(i).split(";")))} for i in content}

# content = {i: {ii: {iii:iii.strip().split(",") for iii in [content.get(i).split(";")[ii - 1]]} for ii in range(1,len(content.get(i).split(";")))} for i in content}

print(content.get(1).get(1).get('blue',0))

# content = {i.split(",") for i in content}