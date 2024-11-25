"""
Excercise 10.7

Question 1: Given a list L and an integer target, you have to find a pair of integers
whose sum is equal to a given integer, target
sample input: L = [1,2,3,4,5] ; target = 9
sample output: (4,5)
"""
"""
Pseudocode

function two_sum(list, target)
    visited[]
    for i = 0 to length(list)
        if visited contains (target - list[i])
            return (target-list[i], list[i])
        endif
        visited.append(list[i])
    endfor
    return null
endfunction
"""

def two_sum( nums, target):
    visited = []

    for i,v in enumerate(nums):
        if (target - v) in visited:
            return (target - v, v)
        visited.append(v)
    return None
        
print(two_sum([1,2,3,4,5], 8))

# visited[]
# for i in nums:
#     if target - v in visited:
#         return 
#
#
#
#
#
