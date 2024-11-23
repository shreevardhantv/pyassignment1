"""
Excercise 10.7

Question 5: Given a list of strings, find out the longest word in that list. Display the
longest word, then replace the longest word with the word “found” and
print the list.
"""

def replace_long(strings: list):
    strings[strings.index(max(strings,key=lambda x: len(x)))] = "found"
    return strings
