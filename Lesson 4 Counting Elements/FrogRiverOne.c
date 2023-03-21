int solution(int X, int A[], int N) {
    int *arr = (int *) calloc(X+1, sizeof(int));
    int count = 0;

    for (int i = 0; i<N; i++)
    {
        if (arr[A[i]] == 0)
        {
            arr[A[i]] = 1;
            count ++;
        }
        if (count == X)
            return i;
    }
    return -1;
}