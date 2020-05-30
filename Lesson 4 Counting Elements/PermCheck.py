def solution(A):
    a= set(A)
    n = len(a)
    if n != len(A):
        return 0
    sum1 = sum(a)
    l = n * (n+1) // 2
    if sum1 == l:
        return 1
    else:
        return 0