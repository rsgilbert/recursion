# C-4.12
# Compute the product of two integers using addition


def product(m, n):
    if n == 1:
        return m
    return m + product(m, n - 1)


## Tests
print(product(3, 5))
print(product(12, 4))