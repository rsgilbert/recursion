## C-4.9
## Find minimum and maximum values in sequence
# Time: O(n)
# Space: O(1) (Cause of tail elimination)

def minimax(S, pos, mini=None, maxi=None):
    if len(S) <= pos:
        return mini, maxi
    if mini is None:
        mini = S[0]
    if maxi is None:
        maxi = S[0]
    return minimax(S, pos+1, min(mini, S[pos]), max(maxi, S[pos]))
    

def mnmx(S):
    return minimax(S, 0)


### Tests
print(mnmx([1, 4, 4, -3, 2]))
print(mnmx([5, 2, 100, 1, 1, 100]))
