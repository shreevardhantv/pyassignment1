"""
Excercise 10.7

Question 11: Input a tuple tup from the user and an integer value k. You should replace
k present in the tuple with the square of that number.
Sample input: tup = (1,2,3,4,5) ; k = 4
Sample output: tup = (1,2,3,16,5)
"""

def tuple_input():
    L = []
    for i in range(int(input("Enter number of items in tuple: "))):
        L.append(int(input(f"Enter element no.{i + 1} :")))
    return tuple(L)

T = tuple_input()
k = int(input("Enter the value of K"))

result = tuple([i**2 if i==k else i for i in T])

print(result)
