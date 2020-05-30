def solution(A):
    A.sort()
    max_pos = A[-1] * A[-2] * A[-3]
    max_neg = float('-inf')
    if A[0] < 0 and A[1] < 0:
        max_neg = A[0] * A[1] * A[-1]
    return max(max_pos, max_neg)