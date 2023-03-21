int solution(int A[], int N) {

    int *arr = (int *) calloc((N+1) , sizeof(int));

    for (int i =0; i<=N; i++)
    {
        arr[A[i] - 1] = 1;
    }

    for (int i =0; i<=N+1; i++)
    {
        if (arr[i] == 0)
            return i+1;
    }
    return 0; // Only to remove the warning
}