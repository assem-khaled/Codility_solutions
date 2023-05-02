import math

def solution(A):
    idx = []        # index of the peaks
    max_flags = 0   # max number of flags used in any iteration so far 

    # Loop to get the indices of the peaks in "idx" list 
    for i in range (1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            idx.append(i)

    max_no_flags = min(len(idx), math.ceil(math.sqrt(len(A))))  # Max number of flags can be either the number of peaks or sqrt(length of array)

    # Loop for the number of the flags to get with you in the backpack
    for flag_no in range(max_no_flags, 0, -1):  
        nxt_flag = idx[0] + flag_no         # The distance between the current and next flag
        flags = 1                           # First flag on the first peak
        flag_counter = flag_no-1            # Number of flags left to set

        # Loop on the peaks' indices to check which peak to set the flags on
        for i in range(1,len(idx)):
            # Check if you have flags left
            if flag_counter == 0:
                break

            # Check if you can set a flag on that peak "idx[i]" according to the rules
            if(idx[i] >= nxt_flag):             
                nxt_flag = idx[i] + flag_no     # Calculate the next availabe peak to set the next flag on according to the rules
                flags += 1                      # Increase the number of flags you have set
                flag_counter -= 1               # Decrement the number of flags you have

        # Check if the number of flags you manage to set is larger than the previous max number
        # If not, then return because we won't be able to set any larger number of flags with any other number of flags we bring with us in the backpack according to the rules
        if flags < max_flags:
            return max_flags
        # If so, then update the "max_flags" 
        elif flags > max_flags:
            max_flags = flags
    
    return max_flags        # Not necessary 