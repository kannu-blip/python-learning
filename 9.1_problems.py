# p1-----
words = {
    "kutta" : "dog",
    "billi" : "cat",
    "suar" : "pig"
}

# word = input("Enter the word you want meaning of: ")
# print(words[word])

# p2-----
# s = set()
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# n = input("Enter the number 1: ")
# s.add(int(n))
# print(s)

# p3-----
s = set()
s.add(18)
s.add("18")
# print(s)

# p4-----
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))

# p5----
s ={}
print(type(s))

# p6----
d = {}
f = (input("Enter the friend name: "))
l = (input("Enter your fvrt language: "))
d.update({f : l})
f = (input("Enter the friend name: "))
l = (input("Enter your fvrt language: "))
d.update({f : l})
f = (input("Enter the friend name: "))
l = (input("Enter your fvrt language: "))
d.update({f : l})
f = (input("Enter the friend name: "))
l = (input("Enter your fvrt language: "))
d.update({f : l})
print(d)
