int solution(int A[], int N) {
    double min = 100001.0;
    int st_indx = 0;

    for(int i=0; i<N-1; i++)
    {
        if ( ((A[i]+A[i+1]) / 2.0) < min )
        {
            min = (double)(A[i]+A[i+1]) / 2.0;
            st_indx = i;
        }
        if ( ( ( (A[i]+A[i+1]+A[i+2]) / 3.0 ) < min) && (i<(N-2)) )
        {
            min = (double)(A[i]+A[i+1]+A[i+2]) / 3.0 ;
            st_indx = i;
        }
    }
    return st_indx;
}