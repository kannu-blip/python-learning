# lists = containers to store set of values of any datatype and Mutable also we can change original list.

list = ["Apple" ,"Orange" ,12 ,34.6 ,False ,"Akash" ,"Rohan"]
print(list[0])

list[0] = "Strawberry"
print(list[0])

print(list[1:5])

list.append("Kannu")
print(list)

l1 = [1 ,0 ,34 ,9 ,22 ,90 ,54]
# l1.sort()
# l1.reverse()
# l1.insert(3 ,3045)
# l1.pop(3)
l1.remove(34)
print(l1)
