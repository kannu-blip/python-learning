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

def gd(name, ending = "thanks"):
    print("Good Day! " + name)
    print(ending)
    return "done"
gd("kinoo", "Thankyouu")
gd("harry")

a = gd("kannu", "Thankyou")
print(a)

# RECURSION - it is a function which calls itself.

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of this number is: {factorial(n)}")

