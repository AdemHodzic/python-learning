# In a string S of lowercase letters, these letters form consecutive groups of the same character.  
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".  
# Call a group large if it has 3 or more characters.  
# We would like the starting and ending positions of every large group.  
# The final answer should be in lexicographic 

def solution(string):
    obj = {}
    arr = []

    unique = list(set(string))
    
    for char in unique:
        obj.update({char: string.count(char)})
    
    for key, val in obj.items():
        if val >= 3:
            temp = []
            first = string.index(key)
            temp.append(first)
            temp.append(first + val - 1)
            arr.append(temp)

    return arr
