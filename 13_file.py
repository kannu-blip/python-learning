# reading 
f = open("13.1_file.txt", "r")
data = f.read()
print(data)
f.close()

# to create a new txt direct
st = "hey kannu you are amazing"
f = open("myfile.txt", "w")

f.write(st)
f.close()

# for readlines
f = open("13.1_file.txt")
lines = f.readlines()

print(lines ,type(lines))