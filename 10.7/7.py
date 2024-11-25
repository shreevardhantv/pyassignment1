"""
Excercise 10.7

Question 7: Write a Python program to accept values from the user. Add it to a tuple
and display the elements one by one. Also, display the maximum and
minimum values of the tuple
"""
"""
Pseudocode

read(tup())

for i = 0 to length(tup)
    print(i, tup[i])

print(max(tup), min(tup))
"""

def tuple_input():
    L = []
    for i in range(int(input("Enter number of items in tuple: "))):
        L.append(int(input(f"Enter element no.{i + 1} :")))
    return tuple(L)

tup = tuple_input()


for i,j in enumerate(tup):
    print(f"Element {i}: {j}")

print(f"Max: {max(tup)}, Min: {min(tup)}")