int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

int solution(int A[], int N) {

    if (N <= 3)
        return 0;

    int *LR = (int*)calloc(N, sizeof(int));
    int *RL = (int*)calloc(N, sizeof(int));

    int max_ending = 0;
    for(int i=1;i<N-1;i++)
    {
        max_ending = max(0, max_ending+A[i]);
        LR[i] = max_ending;
    }

    max_ending = 0;
    for(int i=N-2;i>0;i--)
    {
        max_ending = max(0, max_ending+A[i]);
        RL[i] = max_ending;
    }

    int max_slice = 0;
    for(int i=0;i<N-2;i++)
    {
        max_slice = max(max_slice, LR[i]+RL[i+2]);
    }

    return max_slice;
}