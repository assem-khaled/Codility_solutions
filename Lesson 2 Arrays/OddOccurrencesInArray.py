def solution(A):
    x= 0
    for v in A:
        x ^= v
    return x