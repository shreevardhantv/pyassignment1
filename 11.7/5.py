"""
Excercise 11.7

Question 5: Write a program to find anagrams from a set of n words. An anagram of
a word is another word consisting of the same letters but rearranged in
a different order. (e.g., stop and tops are both anagrams of pots.) The
input consists of n followed by the actual words. The output consists of
anagram sets with each set on different lines. The anagram sets should be
displayed in decreasing order of anagram word lengths. On each line, the
anagrams should be displayed in alphabetical order.

Example Input:
8
stop
tops
pots
opts
dog
god
from
form

Expected Output:
form from
dog god
opts pots stop tops
"""


words = []
n = int(input("Enter amount of words: "))
for _ in range(n):
     word = input("Enter word: ")
     words.append(word)



anagrams = {}
for word in words:
    anagrams.setdefault("".join(sorted(word)), []).append(word)
anagrams = [x for x in anagrams.values() if len(x) >1]
anagrams.sort(key=lambda x: (-len(x[0])))

for i,j in enumerate(anagrams):
        anagrams[i] = sorted(j)

print("\n".join([" ".join(str(j) for j in anagrams[i])for i in range(len(anagrams))]))
