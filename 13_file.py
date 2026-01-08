# READING FILE 
f = open("13.1_file.txt", "r")
data = f.read()
print(data)
f.close()

# TO CREATE A NEW TXT DIRECT
st = "hey kannu you are amazing"
f = open("myfile.txt", "w")

f.write(st)
f.close()

# FOR READLINES
f = open("13.1_file.txt")

# line1 = f.readlines()
# print(line1,type(line1))

# line2 = f.readlines()
# print(line2,type(line2))

# line3 = f.readlines()
# print(line3,type(line3))

# line4 = f.readlines()
# print(line4,type(line4))

line = f.readline()
while (line!=""):
    print(line)
    line = f.readline()
     
f.close()

# FOR APPENDING ANYTHING IN A FILE
st = "Hey harry you are amazing"

f = open("myfile.text","a")
f.write(st)
f.close()


# BY THIS THERE IS NO NEED FOR CLOSE THE FILE
with open(myfile.txt) as f:
    print(f.read())
