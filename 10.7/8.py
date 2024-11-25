"""
Excercise 10.7

Question 8: Write a program to print the Fibonacci sequence using lists
"""
"""
Pseudocode

function fib(n)
    if n <= 0
        return []

    elif n == 1:
        return [0]

    L = [0, 1]
    for i = 2 to n+1
        L.append(L[-1] + L[-2])
    return L

read(n)
result = fib(n)
for i in result
    print(i)
"""

def fib(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    L = [0,1]
    for i in range(2, n + 1):
        L.append(L[-1] + L[-2])
    return L

n = int(input("How many terms of fibonacci sequence do you want: "))
print("\n".join(map(str, fib(n))))
