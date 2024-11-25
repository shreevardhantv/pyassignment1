"""
Excercise 10.7

Question 2: Given a list L, rotate the list k times in the clockwise direction
sample input: L = [1,2,3,4,5] ; k = 2
sample output: [4,5,1,2,3]
"""
"""
Pseudocode

function rotate(list, k)
    k = -(k % length(list))
    return List[k:] + List[:k]
endfunction
"""


def rotate(L, k):
    return L[(k:=-(k%len(L))):] + L[:k]
