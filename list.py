#list=used to store multiple elements in a single variable
#list is ordered, changeable and allows duplicates
students=["johari", "Mary","Brandon","Jane", "Allison"]
mynums=[79,90,67,45,91]
print(students)
print(mynums)
print(type(students))
print(type(mynums))
#len()-length
print(len(students))
print(len(mynums))
#accessing lit items
print(students[0])
print(students[3])
#modifying list item
print(students)
students[1]="Angela"
print(students)
#list methods, append(), remove(), pop()
#append-adds an item at the end
students.append("john")
print(students)
#remove-removes a specific item
students.remove("Jane")
print(students)
#insert()-adds an element at specific index
students.insert(1,"Lewis")
print(students)
#looping through list
for x in students:
 print(x)
