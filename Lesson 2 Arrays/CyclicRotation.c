struct Results solution(int A[], int N, int K) {
    struct Results result;
    // Implement your solution here

    int *temp_arr = (int *)malloc(N * sizeof(int));
    int new_idx = 0;

    for(int i =0; i<N; i++)
    {
        new_idx = K+i;
        new_idx %=  N;
        temp_arr[new_idx] = A[i];
    }

    result.A = temp_arr;
    result.N = N;
    return result;
}