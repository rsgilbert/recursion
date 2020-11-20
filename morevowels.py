# C4.18
# A function to determine if a string has more vowels than consonants


allvowels = 'aeiou'
def morevowels(S, pos, vowelcount, consonantcount):
    if pos < len(S):
        if S[pos] in allvowels:
            return morevowels(S, pos+1, vowelcount+1, consonantcount)
        return morevowels(S, pos+1, vowelcount, consonantcount+1)
    return vowelcount > consonantcount


def mv(S):
    return morevowels(S, 0, 0, 0)


### Tests
print(mv('ababy'))
print(mv('mie'))
print(mv('pipeee'))
print(mv('nymph'))