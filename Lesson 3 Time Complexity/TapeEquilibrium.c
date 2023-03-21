int solution(int A[], int N) {
    
    int sum_after = 0;
    int sum_before = A[0];
    for (int i=1;i<N;i++)
    {
        sum_after += A[i];
    }

    int min_sum = abs(sum_after - sum_before);

    for(int i=1;i<N-1;i++)
    {
        sum_after -= A[i];
        sum_before += A[i];

        if(min_sum > abs(sum_after - sum_before))
            min_sum = abs(sum_after - sum_before);
    }
    return min_sum;
}