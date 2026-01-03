# Sets is the collection of non-repetitive elements

e = set()  # this will create an empty set do not use s{}

s = {1, 3, 6 ,8 ,"kino"}
s.add(56)
print(s)

s.remove("kino")
print(s)

s1 = {1 ,3 ,45 ,6}
s2 = {6 ,78 ,90 ,4}
print(s1.union(s2))

print(s1.intersection(s2))

print(s1-s2)

print({1, 6}.issubset(s1))
