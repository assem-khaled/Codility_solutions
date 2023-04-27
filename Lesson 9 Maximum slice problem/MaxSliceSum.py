# KADANE's Algorithm
def solution(A):
    if len(A) == 1:
        return A[0]
    if max(A) < 0:
        return max(A)

    max_ending = 0
    max_slice = float('-inf')
    for x in A:
        max_ending = max(0, max_ending+x)
        max_slice = max(max_slice, max_ending)
    return max_slice
    

def solution(A):
    max_ending = 0
    max_slice = A[0]
    
    for x in A:
        max_ending = max_ending + x
        max_slice = max(max_slice, max_ending)
        max_ending = max(0, max_ending)
    return max_slice
    
    
# Same concept but generalizes for more than one slice
def solution(A):
    max_ending = 0
    max_slice = [A[0]]*len(A)
    
    for i in range(len(A)):
        max_ending = max_ending + A[i]
        max_slice[i] = max_ending
        max_ending = max(0, max_ending)
        
    return max(max_slice)