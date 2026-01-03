a = int(input("Enter your age: "))

if(a>18):
    print("you're are eligible")

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("You're entering age 0 which is not valid")

else:
    print("you're not eligible")

print("End of program")