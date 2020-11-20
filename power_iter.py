# 4.22
# Power with repeated squaring implemented without recurssion


def power_iter(x, n):
    res = x
    power = 1

    while 2 * power <= n:
        res *= res
        power *= 2

    while power < n:
        res *= x
        power += 1

    return res



# Tests
print(power_iter(2, 5))
print(power_iter(3, 5))
print(power_iter(4, 4))
print(power_iter(5, 2))


    
    
