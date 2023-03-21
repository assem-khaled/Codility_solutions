def solution(A):
    l = set( range(1, len(A)+2))
    
    for i in A:
        l.remove(i)
    
    return l.pop()
  
  
def solution(A):
    l = [0] * (len(A)+1)

    for i in A:
        l[i-1] = 1
    
    return l.index(0)+1

        
def solution(A):
    try:
        A.sort()
        i2=1
        for i in A:
            if i != i2:
                return i2
            else:
                i2+=1
    
        return A[-1] + 1
    except:
        #no elements in the list
        return 1
		
