"""
Excercise 10.7

Question 7: Write a Python program to accept values from the user. Add it to a tuple
and display the elements one by one. Also, display the maximum and
minimum values of the tuple
"""

def tuple_input():
    L = []
    for i in range(int(input("Enter number of items in tuple: "))):
        L.append(int(input(f"Enter element no.{i + 1} :")))
    return tuple(L)

tup = tuple_input()

