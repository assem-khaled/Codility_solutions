def fib_no(n):
    fib = [0]
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def solution(A, B):
    result = [0] * len(A)

    fib = [0] 
    fib.append(1)

    for i in range(2, len(A)+2):
        fib.append(fib[i-1] + fib[i-2]) 
    
    for i in range(len(A)):
        result[i] = fib[A[i]+1] & (2**B[i]-1)
    # https://stackoverflow.com/questions/6670715/mod-of-power-2-on-bitwise-operators/6670766#6670766
    # Best explains why bitwise & is faster than mod for this calculation.
    return result