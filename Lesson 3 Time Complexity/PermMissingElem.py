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
		
def solution2(A):
    n = len(A)
    a =[0] * n

    for i in A:
        if 1 <= i <= n:
            a[i-1] = 1
    try:
        return a.index(0)+1
    except:
        return len(A)+1