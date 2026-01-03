# n = int(input("Enter the value: "))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

# p2----
# n = int(input("Enter the value: "))
# for i in range(1,n+1): 
#     print("*"*i, end="")
#     print("")

# p3---
# n = int(input("Enter the value: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#       print("*"*(n),end="")
#     else:
#       print("*",end="")
#       print(" "*(n-2),end="")
#       print("*",end="")
#     print("")

# p4----
n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")
 