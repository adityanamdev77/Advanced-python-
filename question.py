#WAP to create a list of movies and add 3 movies to the list using append function and print the list.

movies = [1]
mov1 = input("enter the 1st movie: ")
mov2 = input("enter the 2nd movie: ")
mov3 = input("enter the 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#WAP tocheck if a list contain a palindrome of element.hint:use copy()method)

list1 = [1,2,3,2,1]
list2 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list2:
    print("the list is palindrome")
    
#WAP to count the number with the "A" grade in the following tuple.

grade = ("A","B","C","A","D","A","B")
print(grade.count("A"))

#store the above valuies in a list & sort them from "A" to "d"

grade = ["A","B","C","A","D","A","B"]
grade.sort()
print(grade)