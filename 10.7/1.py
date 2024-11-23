"""
Excercise 10.7

Question 1: Given a list L and an integer target, you have to find a pair of integers
whose sum is equal to a given integer, target
sample input: L = [1,2,3,4,5] ; target = 9
sample output: (4,5)
"""

def two_sum( nums, target):
    visited = []

    for i,v in enumerate(nums):
        if (target - v) in visited:
            return [visited.index(target-v),i]
        visited.append(v)
        
        