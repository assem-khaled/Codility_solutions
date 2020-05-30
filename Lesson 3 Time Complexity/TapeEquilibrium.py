def solution(A):
    sum_after = sum(A[1:])
    sum_befor = A[0]
    min_sum = abs(sum_after - sum_befor)
    for i in range(1,len(A)-1):
        sum_after -= A[i]
        sum_befor += A[i]

        if min_sum > abs(sum_after - sum_befor):
            min_sum = abs(sum_after - sum_befor)
    return min_sum
	
def solution2(A):
    sum_befor = A[0]
    sum_after = sum(A[1:])
    min_sum = abs(sum_befor - sum_after)
    for i in A[1:-1]:
        sum_after -= i 
        sum_befor += i

        
        if min_sum > abs(sum_befor - sum_after):
            min_sum = abs(sum_befor - sum_after)
    return min_sum