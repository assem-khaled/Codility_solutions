// KADANE's Algorithm
int solution(int A[], int N) {
	if(N == 1)
        return A[0];
	
	// Check if all numbers are negative
    int max = -2147483648;
    for(int i=0;i<N;i++)
    {
        if(max<A[i])
            max = A[i];
    }
    if(max<0)
        return max;
    
	// The code below can't handle array of negative numbers ex: [-10], [-10,-100]
    int max_ending = 0, max_slice = -2147483648;
    for(int i=0;i<N;i++)
    {
        if(max_ending+A[i] > 0)
            max_ending = max_ending+A[i];
        else
            max_ending = 0;
        
        if(max_ending > max_slice)
            max_slice = max_ending;
    }
    return max_slice;
}


int solution(int A[], int N) {
    int max_ending = 0, max_slice = A[0];
	
    for(int i=0;i<N;i++)
    {
        max_ending = max_ending+A[i];

        if(max_ending > max_slice)
            max_slice = max_ending;

        if(max_ending < 0)
            max_ending = 0; 
    }
    return max_slice;
}