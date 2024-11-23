"""
Excercise 10.7

Question 8: Write a program to print the Fibonacci sequence using lists
"""

def fib(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    L = [0,1]
    for i in range(n-2):
        L.append(L[-1] + L[-2])
    return L
