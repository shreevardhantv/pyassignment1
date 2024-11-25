"""
Excercise 10.7

Question 3: Write a Python program that inputs a list of numbers and then doubles
the odd numbers and halves the even numbers
"""
L = []
for i in range(int(input("Enter number of items in list: "))):
    n = int(input(f"Enter {i}"))
    L.append(2*n if n%2 else n/2)

print(L)