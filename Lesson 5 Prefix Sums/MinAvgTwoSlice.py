def solution(A):
    min = float("inf")
    min_idx = 0
    for i in range(len(A)-1):
        if (A[i]+A[i+1])/2 < min:
            min = (A[i]+A[i+1]) / 2
            min_idx = i
    for i in range(len(A) - 2):
        if (A[i]+A[i+1]+A[i+2])/3 < min:
            min = (A[i]+A[i+1]+A[i+2]) / 3
            min_idx = i
    return min_idx

def solution2(A):
    min_idx = 0
    min_value = 10001
 
    for idx in range(0, len(A)-1):
        if (A[idx] + A[idx+1])/2.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1])/2.0
        if idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1] + A[idx+2])/3.0
 
    return min_idx