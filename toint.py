# Convert a string of digits to an integer

## Complexity
## Time: O(n)
## Space: O(n)
def toint(S, pos):
    if pos >= len(S):
        return 0
    return int(S[pos]) * (10 ** (len(S) - 1 - pos)) + toint(S, pos + 1)


############
## Tests ##
print(toint('142', 0))
print(toint('8431', 1))