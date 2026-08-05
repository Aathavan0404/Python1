Marks = [85, 92, 78, 96, 88]
Total = 0
for mark in Marks:
    Total += mark  #Total = Total + mark
Average = Total / len(Marks) # len means length of the list
print(f"The average is {Average: .2F}")


print(Marks[3])  # Accessing the fourth element in the list (index 3)
print(Marks[-1])  # Accessing the last element in the list (index -1)
#Count starts from 0, so the first element is at index 0, the second at index 1, and so on. Negative indexing starts from the end of the list, with -1 being the last element, -2 being the second last, and so on.