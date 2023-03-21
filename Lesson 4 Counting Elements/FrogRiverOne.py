def solution(X, A):
    s = set()

    for i in range(len(A)):
        s.add(A[i])
        if len(s) == X:
            return i

    return -1  

def solution(X, A):
    list = set()
    for i in range(1 , X+1):
        list.add(i)

    for i in A:
        try:
            list.remove(i)
        except:
            pass
        if  len(list) ==0:
            return A.index(i)
    return -1