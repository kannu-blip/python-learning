# p1-----
def greatest(a ,b ,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 1
b = 23
c = 8
print(greatest(a,b,c))

# p2----
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in f: "))
print(f"{f_to_c(f)}°C")