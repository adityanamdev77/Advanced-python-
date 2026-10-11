from operator import add


info = {
    "name" : "aditya",
    "key" : "value",
    "learning" : "coding"
}

info["name"] = "aditya namdev"
print(info)

#nesting in dict.

student = {
    "name": "aditya",
    "subjects": {
        "maths": 90,
        "science": 95,
        "english": 85
    }
}

print(student["subjects"]["maths"])

#sets add method

collection = set()

collection.add(1)
collection.add(2)

print(collection)   

#set union 

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
