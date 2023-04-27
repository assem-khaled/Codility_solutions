int solution(int A[], int N) {
    int count = 0;
    int multiply = 0;

    for(int i=0;i<N;i++)
    {
        if(A[i] == 0)
		{
            multiply++;
		}
        
        if(multiply>0)
        {
            if(A[i] == 1)
            {
                count += multiply;
                if(count > 1000000000)
				{
                    return -1;
				}
            }
        }
    }
    return count;
}