# Recursive program for finding the maximum element in a sequence


def maximum(S, pos = 0, maxi=None):
    if pos < len(S):
        if maxi is None:
            maxi = S[pos]
        return maximum(S, pos + 1, max(maxi, S[pos]))
    return maxi


def mx(S):
    return maximum(S, 0, None)

#########################################
# Tests


print(mx([1, 3, 4, 2]))
print(mx([]))
print(mx([1]))
print(mx([199, 223, 4]))


