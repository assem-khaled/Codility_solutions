def solution(A):
    x= 0
    for v in A:
        x ^= v
    return x
    
    
    
def solution(A):
    x = set()
    
    for i in A:
        if i in x:
            x.remove(i)
        else:
            x.add(i)
 
    return x.pop()