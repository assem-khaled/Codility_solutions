int solution(int A[], int N) {
    int size = 0, candidate = 0, value = 0, count = 0;

    for(int i=0;i<N;i++)
    {
        if(size == 0)
        {
            size++;
            value = A[i];
        }
        else 
        {
            if(value != A[i])
                size--;
            else 
                size++;
        }
    }

    if(size > 0)
        candidate = value;
    else
        return -1;
    
    for(int i=0;i<N;i++)
    {
        if(candidate==A[i])
        {
            count++;
            if(count > (N/2))
                return i;
        }
    }
    return -1;
}