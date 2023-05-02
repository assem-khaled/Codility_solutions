import math

def solution(N):
    i = math.floor(math.sqrt(N))
    
    while(i>0):
        if N%i == 0:
            return int (2* (i + (N/i)))
        i -= 1