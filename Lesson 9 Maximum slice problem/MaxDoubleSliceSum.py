def solution(A):
    if len(A) <= 3:
        return 0

    LR = [0] * len(A)
    RL = [0] * len(A)

    max_ending = 0
    for i in range(1, len(A)-1):
        max_ending = max(0 ,max_ending + A[i])
        LR[i] = max_ending
    
    max_ending = 0
    for i in range(len(A)-2, 0, -1):
        max_ending = max(0 ,max_ending + A[i])
        RL[i] = max_ending

    max_slice = 0
    for i in range(0, len(A)-2):
        max_slice = max(max_slice, LR[i]+RL[i+2])
    
    return max_slice