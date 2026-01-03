# p1-----
# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1 >a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1: ",a1)
# elif(a2 >a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2: ",a2)
# elif(a3 >a2 and a3>a1 and a3>a4):
#     print("Greatest number is a3: ",a3)
# if(a4 >a2 and a4>a3 and a4>a1):
#     print("Greatest number is a4: ",a4)

# p2-----
marks1 = int(input("Enter marks of Science1: "))
marks2 = int(input("Enter marks of Maths2: "))
marks3 = int(input("Enter marks of Hindi3: "))
marks4 = int(input("Enter marks of English4: "))
marks5 = int(input("Enter marks of SST5: "))

total_percentage = (marks1 + marks2 + marks3 + marks4 + marks5)*100/500
print(total_percentage)
if(total_percentage>=40):
    print("You are pass!")
else:
    print("You are fail try again!")


# p3-----
# p = "make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ")

# if((p in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this message is spam")
# else:
#     print("This message is not spam")


# p4-------
# name = input("Enter your username: ")
# if(len(name)<10):
#     print("your name char is less than 10")
# else:
#     print("your name char is well!")

# p5-------
# l1 = ["kannu", "Riya" , "Annu","Ayush"]
# name = input("Enter your name: ")
# if(name in l1):
#     print("your name is in list")
# else:
#     print("Your name is not in the list")


# # p6-------
# marks = int(input("Enter your marks: "))
# if(marks<=100 and marks>=90):
#     print("your grade is excillent")
# elif(marks<=90 and marks>=80):
#     print("Your grade is 'A'")
# elif(marks<=80 and marks>=70):
#     print("Your grade is 'B'")
# elif(marks<=70 and marks>=60):
#     print("Your grade is 'C'")
# elif(marks<=60 and marks>=50):
#    print("Your grade is 'D'")
# else:
#    print("Your grade is 'F'")

# # p7-------
# post = input("Enter your post: ")
# if("Kannu".lower() in post.lower()):     # lower is for if name is in mix capital or lower it'll detected
#     print("This post is talking about you")
# else:
#     print("This post is not about you")

