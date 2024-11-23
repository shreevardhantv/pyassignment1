"""
Excercise 10.7

Question 4: Given a list nums of numbers and an integer val, remove all occurrences
of val in the list.
sample input: nums = [1,2,2,3,4,5,6,6,2,2,2,8] ; val = 2
sample output: [1,3,4,5,6,6,8]
"""

def remove_val(nums, val):
    return [i for i in nums if i!= val]
