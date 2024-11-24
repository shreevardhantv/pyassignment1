"""
Excercise 11.7

Question 2: Write a program to read N words and group the words by their length in
a dictionary. (The dictionary should have the length of the words as keys
and sets of words of that length as values.)

Example Input:
N = 6
Words = ["Hello", "World", "This", "Apple", "Banana", "Program"]

Expected Output:
{4: {"This"}, 5: {"Hello", "World", "Apple"}, 6: {"Banana"},
7: {"Program"}}
"""

words = input("Enter words: ").split()
lengths = dict()

for i in words:
    lengths.setdefault(len(i), set()).add(i)

print(lengths)

