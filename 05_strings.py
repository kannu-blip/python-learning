name = "kannu"

index = name[0:3]
print(index)

print(name[-4:-1])

print(name[ :4])    #means it is starting from index 0

print(name[1: ])    #means it is ending with full length of string

words = "abcdefghijklmnop"
print(words[1:7:4])      #start ,end ,skip/gap

#------- functions of strings-----
print(len(name))

print(name.endswith("nu"))

print(name.startswith("ka"))

count = name.count("n")
print(count)

capitalized_string = name.capitalize()
print(capitalized_string)

s = "hello world"
find = s.find("world")
print(find)

replace = s.replace("world" ,"python")
print(replace)

# -----Escape Characters------------
# \n (new line), \t(tabspace), \"\"(double quote), \\(backslash)
a = "hello this is the python\nescape characters which is very\n \"intrested\""
print(a)