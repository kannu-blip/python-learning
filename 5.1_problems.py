# p1-------
a = input("Enter your name: ")
# print("Good Afternoon",a)
#     OR
print(f"Good Afternoon {a}")

# p2---------
letter = '''Dear <|Name|>,
youre selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Kannu").replace("<|Date|>", "29 sept 2026"))

# p3----
name = "this is to find double  space "
print(name.find("  "))

# p4------
print(name.replace("  "," "))     #in this line is printed new line but didnt change original name line

# p4-----
escape = ("Dear kannu!\n\tThis course is for python programming\nThanks!")
print(escape)