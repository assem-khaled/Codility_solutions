int solution(int H[], int N) {
    if(N == 1)
        return 1;

    int stones = 1;
    int *hights = (int*)calloc(N,sizeof(int));
    hights[0] = H[0];
    int len_hights = 1;

    for (int i =1; i<N;i++)
    {
        if(H[i] < H[i-1])
        {
            while((len_hights > 0) && (H[i]<hights[len_hights-1]))
            {
                len_hights--;
            }
            if((len_hights==0) || (H[i]!=hights[len_hights-1]))
            {
                stones += 1;
                hights[len_hights] = H[i];
                len_hights++;
            }
        }
        else if(H[i] > H[i-1])
        {
            stones++;
            hights[len_hights] = H[i];
            len_hights++;
        }
    }
    return stones;
}