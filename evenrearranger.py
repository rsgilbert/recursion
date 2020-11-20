# 16:38 hrs, 20th November 2020
# C4.19
# Arranges a sequence so that all evens come before odds
# Time: O(n)


def evenrearranger(S, pos):
    if pos < len(S):
        if S[pos] % 2 == 0 and pos > 0 and S[pos - 1] % 2 == 1:
            S[pos - 1], S[pos] = S[pos], S[pos - 1]
            evenrearranger(S, pos - 1)
        else:
            evenrearranger(S, pos + 1)


def ev(S):
    return evenrearranger(S, 0)


### Tests
S1 = [1, 2, 3, 4, 5, 6, 7]
S2 = [2, 4, 6]
S3 = [1, 3, 5, 100, 200]
S4 = [-11, 13]

ev(S1)
ev(S2)
ev(S3)
ev(S4)

print(S1)
print(S2)
print(S3)
print(S4)
