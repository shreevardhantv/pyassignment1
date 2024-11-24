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


def is_anagram(word1, word2):
    f1 = {}
    for i in word1:
        f1.setdefault(i, 0)
        f1[i] += 1

    f2 = {}
    for i in word2:
        f2.setdefault(i, 0)
        f2[i] += 1
    
    return f1==f2


def find_anagrams(words):
        out = {}
        for word in words:
            out[tuple(sorted(list(word)))] = [i for i in words if (
                is_anagram(i,word)
            )]
            
        out = [i for i in out.values() if len(i)!= 1]

        out.sort(key=lambda x: (-len(x[0])))

        for i,j in enumerate(out):
             out[i] = sorted(j)
        return out

words = []
n = int(input("Enter amount of words: "))
for _ in range(n):
     word = input("Enter word: ")
     words.append(word)

out = find_anagrams(words)
print("\n".join([" ".join(str(j) for j in out[i])for i in range(len(out))]))



