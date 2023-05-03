def calc_fib_no(N):
    fib = [0] 
    fib.append(1)

    for i in range(2, N+2):
        fib.append(fib[i-1] + fib[i-2]) 
        if fib[i] > N:
            fib.pop() # Discard the last inserted element
            break

    fib.remove(0)
    fib.remove(1)
    
    return fib


def solution(A):
    if len(A) == 0:     # If empty list then return 1 (can jump to the other river bank)
        return 1
    n = len(A)

    fib_no =calc_fib_no(n+1)

    leaves_found = {-1}   # Define a set contains the leaves already found with the initial position (-1 -> the river bank)
    
    for iteration_no in range(1, n+1):
        next_iter_learves = set()
        for pos in leaves_found:
            for jump in fib_no:
                if pos + jump == n:                         # Can jump to the other bank ?
                    return iteration_no
                if pos + jump < n and A[pos + jump] == 1:   # There is a leave in that postition
                    next_iter_learves.add(pos + jump)

        leaves_found = next_iter_learves                     # Save the leaves found for next iterations
    
    return -1
    
## Another solution 100% Correctness and 50% Performance
def solution(A):
    if len(A) == 0:
        return 1
    A.append(1)

    ## Calculate Fibonacci numbers
    n = len(A)
    fib = [0] 
    fib.append(1)

    for i in range(2, n+2):
        fib.append(fib[i-1] + fib[i-2]) 
        if fib[i] > n:
            fib.pop() # Discard the last inserted element
            break

    fib_set = set(fib)
    fib_set.discard(0)
    ## End

    steps = [0] * len(A)
    # Can be reached with one jump / First jump
    for i in fib_set:
        if A[i-1] == 1:
            steps[i-1] = 1

    # Can be reached with more than one jump
    s = 1
    while s < len(A):
        for i in range(0, len(A)):
            if A[i] == 1 and steps[i] == 0:  
                for j in range(0, len(fib)):
                    if i - fib[j] >= 0:
                        if steps[i - fib[j] ] == s:
                            steps[i ] = s+1
        s += 1
        if steps[-1] != 0:
            return steps[-1] 
            
    return -1
    