"""
Excercise 10.7

Question 3: Write a Python program that inputs a list of numbers and then doubles
the odd numbers and halves the even numbers
"""
"""
Pseudocode

numbers[]
read(n) // Number of input values
for i = 0 to n
    read(num)
    if num%2 == 1
        numbers.append(2*num)
    else
        numbers.append(num/2)
    endif
endfor
print(numbers)


"""

L = []
for i in range(int(input("Enter number of items in list: "))):
    n = int(input(f"Enter element no.{i}: "))
    L.append(2*n if n%2 else n//2)

print(L)

