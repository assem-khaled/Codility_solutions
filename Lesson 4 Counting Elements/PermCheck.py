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


# Slower
def solution(A):
    s =set(range(1,len(A)+1))

    for i in A:
        if i > len(A):
            return 0

        s.discard(i)

        if len(s) == 0:
            return 1
    
    return 0