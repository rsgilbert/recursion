## C-4.11
## Solve element uniqueness
## Time: O(n ** 2)
## Space: O(1)



def unique(S, i, j):
    if i >= len(S):
        return True
    if j >= len(S):
        return unique(S, i+1, 0)
    if S[i] == S[j] and i != j:
        ## Found a match
        return False
    return unique(S, i, j+1)

def uniq(S):
    return unique(S, 0, 0)
### Tests
print(uniq([1, 2, 3, 4, 5]))
print(uniq([5, 3, 5, 2]))
print(uniq([10, 4, 2, 5]))
print(uniq([5, 9, 3, 1, 10, 3]))