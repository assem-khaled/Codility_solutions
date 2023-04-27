def solution(A):
    candidate = -1
    d = dict()

    for i in A:
        d[i] = 0
    
    for i in A:
        d[i] = d[i] + 1
    
    for k,v in d.items():
        if v > (len(A)/2):
            return A.index(k)

    return -1
    
# Solution found in the reading material
# Same time complixty
def solution(A):
    size = 0

    for i in range(len(A)):
        if(size==0):
            size += 1
            value = A[i]
        else:
            if(value != A[i]):
                size -= 1
            else:
                size += 1
    
    if size > 0:
        candidate = value
    else:
        return -1

    count = 0

    for i in range(len(A)):
        if candidate == A[i]:
            count += 1
            if count > (len(A)/2):
                return A.index(candidate)   # same as i

    return -1