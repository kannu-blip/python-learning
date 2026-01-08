# p1-----
f = open("myfile.txt")
data = f.read()
if("twinkle" in data):
    print("twinkle is present in the file")
else:
    print("twinkle is not present in the file")

f.close()

# p2-----
import random
def game():
    print("Game start...")
    score = random.randint(1,62)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(score)
        else:
            hiscore = 0

    print(f"Your score is :{score}")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()

# p3----
def generatetable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} * {i} = {n*i}\n"

    with open(f"13.3_tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,12):
    generatetable(i)

# p4------
words = ["donkey" ,"gadha"]
with open("myfile.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "#"*len(word))

with open("myfile.txt", "w") as f:
    f.write(content)


# p5------
with open("log.txt") as f:
    content = f.read()

if ("PYTHON" in content):
    print("Yes! python is in content")
else:
    print("No! python is not in content")

