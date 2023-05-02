import math 

def solution(N):
    count = 0
    i = 1
    while(i*i < N):
        if (N%i) == 0:
            count += 2
        i += 1

    if (i*i == N):
        count += 1
    
    return count


def solution(N):
    count = 0
    i = 0
    for i in range(1, math.ceil(math.sqrt(N))):
        if (N%i) == 0:
            count += 2
    
    i += 1
    if (i*i == N):
        count += 1
    
    return count