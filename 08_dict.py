# dictionaries is the collection of key value pairs
marks = {
    "kannu" : 80,
    "shiv" : 76,
    "rohan" : 34
}
print(marks,type(marks))
print(marks["kannu"])

print(marks.items())

print(marks.keys())

print(marks.values())

up = marks.update({"kannu": 94, "riya" : 37})

print(marks.get("kannu2"))  #returns the none value
# print(marks["kannu2"])  #returns error

value = marks.pop("rohan")
print(marks)

item = marks.popitem()     #last item pop 
print(marks)