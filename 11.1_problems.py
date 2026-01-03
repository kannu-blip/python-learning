# p1---- for any table 
# n = int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{n}* {i} = {n * i}")

# p2------
# l1 = ["kannu", "ayush" ,"karan" ,"keshav"]
# for name in l1:
#     if(name.startswith("k")):
#      print(f"Hello {name}")

# p3----
# n = int(input("Enter the number: "))
# i = 1
# while(i<11):
#     print(f"{n} * {i} = {i*n}")
#     i = i+1

# p4-----
# n = int(input("Enter the number: "))
# for i in range(2,n):
#     if(n%i == 0):
#         print("Number is not prime")
#         break
# else:
#         print("Number is prime")

# p5-----
# n = int(input("Enter the number: "))
# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)

# p6-----
n = int(input("Enter the value: "))
product = 1
for i in range(1, n+1):
     product = product*i
print(f"The factorial of {n} is {product}")
