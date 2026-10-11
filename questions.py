#store following word meaning in a python dictionary

dict = {
    "table" : ["a piece of furnitur","list of facts & figures"],
    "cat"  :" a small animal",
}

print(dict)

#you are given a list of subjects for students.assume one classroom is required for 1 subjecty.how many classroom are neede by all students.

subjects ={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}

print(subjects)
print(len(subjects))

#WAP to enter of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & add one by one.use subjects name as key & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy":x})

x = int(input("enter chem : "))
marks.update({"chem":x})

x = int(input("enter maths : "))
marks.update({"maths":x})

print(marks)
