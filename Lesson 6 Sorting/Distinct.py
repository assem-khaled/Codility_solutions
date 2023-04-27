def solution(A):
    if len(A) == 0:
        return 0

    A.sort()
    result = 1
    
    for i in range(len(A)-1):
        if(A[i] != A[i+1]):
            result += 1
    return result