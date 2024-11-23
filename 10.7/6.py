"""
Excercise 10.7

Question 6: Write a Python program to input any two tuples and swap them.
Sample input: tuple1 = (1,2,3,4,5) ; tuple2 = (10,20,30,40,50)
Sample output: tuple1 = (10,20,30,40,50) ; tuple2 = (1,2,3,4,5)
"""

def tuple_input():
    L = []
    for i in range(int(input("Enter number of items in tuple: "))):
        L.append(int(input(f"Enter element no.{i + 1} :")))
    return tuple(L)


tuple1, tuple2 = tuple_input(), tuple_input()

tuple2, tuple1 = tuple1, tuple2

print(f"tuple1={tuple1},tuple2={tuple2}")