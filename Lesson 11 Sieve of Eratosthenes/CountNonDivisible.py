## The Explanation of this solution can be found here
## https://www.youtube.com/watch?v=tImgeYTHdAU&t=896s

import math

def solution(A):
    
    non_div = []
    non_div_dict = {}
    max_elem = max(A)
    counts = [0] * (max_elem + 1 )

    for i in A:
        counts[i] += 1
    
    setof_A = set(A)
    for i in setof_A:
        divisors = 0

        for j in range(1, math.floor(math.sqrt(i))+1):
            if i%j ==0:
                divisors +=  counts[j]

                if(int(i/j)!=j):
                    divisors +=  counts[int(i/j)]
        
        non_div_dict[i] = (len(A)- divisors)
    
    for i in A:
        non_div.append(non_div_dict[i])

    return non_div