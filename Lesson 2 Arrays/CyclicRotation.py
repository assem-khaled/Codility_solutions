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
        
def solution(A, K):

    temp_list = [0] * len(A)
    new_idx = 0
    
    for i in range(len(A)):
        new_idx = K+i
        new_idx %= (len(A))
        temp_list[new_idx] = A[i]
    
    return temp_list