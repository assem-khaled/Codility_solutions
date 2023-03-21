def solution(A):
    sum_after = sum(A[1:])
    sum_before = A[0]
    min_sum = abs(sum_after - sum_before)
    for i in range(1,len(A)-1):
        sum_after -= A[i]
        sum_before += A[i]

        if min_sum > abs(sum_after - sum_before):
            min_sum = abs(sum_after - sum_before)
    return min_sum
	
def solution2(A):
    sum_before = A[0]
    sum_after = sum(A[1:])
    min_sum = abs(sum_before - sum_after)
    for i in A[1:-1]:
        sum_after -= i 
        sum_before += i

        
        if min_sum > abs(sum_before - sum_after):
            min_sum = abs(sum_before - sum_after)
    return min_sum