int solution(int A[], int N) {
    
    int x = 0;
    for(int i = 0; i<N; i++)
    {
        x ^= A[i];
    }
    return x;
}