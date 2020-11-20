# Compute the nth harmonic number


def harmonic(n):
    if n == 1:
        return 1
    return 1 / n + harmonic(n - 1)

######################
## Tests ###
print(harmonic(3))
print(harmonic(4))