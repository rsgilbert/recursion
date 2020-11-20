## C-4.10
## Compute integer part of log2 of n using addition and integer division

## Time: O(log(n))
## Space: O(1)

def mylog(n):
    if n <= 1:
        return 0
    return 1 + mylog(n // 2)


#### Tests
print(mylog(14))
print(mylog(5))