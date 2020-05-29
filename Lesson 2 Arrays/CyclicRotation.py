def solution(A, K):
    try:
        list = A
        
        while K >0:
            temp = list[-1]
            
            i=len(list)-1
            while i >= 0:
                list[i] = list[i-1]
                i-=1
            list[0] = temp
            K-=1
        return list
    except:
        return A