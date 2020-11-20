# C-4.17
# Function that checks if given string is a palindrome


def ispalindrome(S, start, end):
    if start < end:
        if S[start] != S[end]:
            return False
        return ispalindrome(S, start + 1, end - 1)
    return True

def isp(S):
    return ispalindrome(S, 0, len(S) - 1)

## Tests

print(isp('goog'))
print(isp('drink'))
print(isp('gohangasalamiimalasagnahog'))
print(isp('babab'))
print(isp('chathc'))