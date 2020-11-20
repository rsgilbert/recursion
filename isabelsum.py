### R-4.8
### Compute the sum of a sequence with 2 ** n items
## Running time: O(nlog(n))
## Space usage: O(log(n))
def isabelsum(A):
    if len(A) == 1:
        return A[0]
    B = []
    for i in range(len(A) // 2):
        B.append(A[2 * i] + A[2 * i + 1])
    return isabelsum(B)


########
## Tests
print(isabelsum([2, 3, 1, 7]))
print(isabelsum([8, 10]))
print(isabelsum([1, 2, 3, 4, 5, 6, 7, 8]))
print(isabelsum([3]))