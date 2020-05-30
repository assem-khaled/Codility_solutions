def solution(A):
    A.sort()
    if len(A) == 0:
        return 0
    d = 1
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            d += 1
    return d