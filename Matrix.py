for row in range (1,4):
    for col in range (1,4):
        print(row*col, end = " ") #end means that the next print statement will be printed on the same line, separated by a space
    print()  # This will print a new line after each row is printed

print()  

for row in range(3): #3 means that the loop will run 3 times, with row taking values 0, 1, and 2
    for col in range (1,4): #loop will stop at 4, so col will take values 1, 2, and 3
        print(row+col, end = " ")
    print()  


Marks = [85, 92, 78, 96, 88]
Subjects = ["Maths", "Science", "English", "History", "Geography"]
Mixed = [76, "Aathi", 3.14, True, None, [1,2,3], {"Name":"Aathi","Age":20}] #List can contain different data types, including integers, strings, floats, booleans, None, other lists, and dictionaries.

Marks[2] = 80  # Modifying the third element in the list (index 2)
print(Marks[2])

Marks.append(23)  # Adding a new element to the end of the list .....Add to the end.....
Marks.insert(2, 90)  # Inserting a new element at index 2 
Marks.remove(92)  # Removing the first occurrence of the value 92 from the list
Marks.pop()  # Removing the last element from the list
Marks.sort()  # Sorting the list in ascending order
Marks.reverse()  # Reversing the order of the list
Marks.clear()  # Removing all elements from the list
print(Marks) 