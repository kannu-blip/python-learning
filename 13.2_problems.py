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

    print(f"Your score is : {score}")
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

# p6-----
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("PYTHON" in line):
        print(f"yes python is present in line no: {lineno}")
        break
    lineno += 1

else:
       print("No python is not present")
    
# p7----
with open("myfile.txt") as f:
    content1 = f.read()

with open("log.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No these file are not identical")

# p8----
# with open("log.txt", "w") as f:     
#     f.write("")                         #this will wipe out all code existing in it