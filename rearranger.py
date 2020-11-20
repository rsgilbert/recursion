# C-4.20
# Rearrange so that all elements < k come before 
# any element > k
# Time: O(n)

def rearranger(S, k, pos=0):
    if pos < len(S):
        if S[pos] <= k and pos > 0 and S[pos - 1] > k:
            S[pos - 1], S[pos] = S[pos], S[pos - 1]
            rearranger(S, k, pos - 1)
        else:
            rearranger(S, k, pos + 1)


## Tests
S1 = [4, 5, 6, 7, 1, 2, 3, 4, 7]
S2 = [10, 11, 2, 4, 6]
S3 = [3, 1000, 113, 5, 100, 200]
S4 = [-100, 44, -11, 13]

rearranger(S1, 4)
rearranger(S2, 4)
rearranger(S3,5)
rearranger(S4, 10)

print(S1)
print(S2)
print(S3)
print(S4)
