# C-4.21
# Find two integers that sum to k
# S is sorted with distinct integers
# Time: O(n ** 2)

def summatch(S, k, i=0, j=0):
    if i >= len(S):
        return None
    if j >= len(S):
        return summatch(S, k, i + 1, 0)
    if S[i] + S[j] == k:
        return S[i], S[j]
    if S[i] + S[j] > k:
        return summatch(S, k, i + 1, 0) 
    if S[i] + S[j] < k:
        return summatch(S, k, i, j + 1)
    return None



# Tests
print(summatch([1, 2, 3, 5, 17], 8))
print(summatch([1, 1, 4, 5, 5], 9))
print(summatch([-1, 2, 3, 4, 5], 5))
print(summatch([-1, 2, 3, 4, 5], 65))