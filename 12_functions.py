     # Function - It is a group of statements which performs a specific tasks.

# Function definition
def avg():
    a = int(input("Enter the value: "))
    b = int(input("Enter the value: "))
    c = int(input("Enter the value: "))
    average = (a + b + c/3)
    print(average)

# avg()     #Function call
# avg()

def gd(name, ending):
    print("Good Day! " + name)
    print(ending)
    return "done"
gd("kinoo", "Thankyouu")
gd("harry", "thnkyouuu")

a = gd("kannu", "Thankyou")
print(a)
