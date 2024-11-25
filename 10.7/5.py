"""
Excercise 10.7

Question 5: Given a list of strings, find out the longest word in that list. Display the
longest word, then replace the longest word with the word “found” and
print the list.
"""
"""
Pseudocode
function replace_long(strings)
    max_length = 0
    max_index = 0
    
    for i = 0 to length(strings)
        if length(strings[i]) > max_length
            max_length = length(strings[i])
            max_index = i
        endif
    endfor
    print(strings[max_index])
    strings[max_index] = "found"
    print(strings)
endfunction
"""

def replace_long(strings):
    max_index = strings.index(max(strings,key=lambda x: len(x)))
    print(strings[max_index])
    strings[max_index] = "found"
    print(strings)