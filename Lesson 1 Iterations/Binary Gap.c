#define git_bit(var,bit_no)     (( var >> bit_no ) & 1)


int solution(int N) {
    
    int bit = 0, flag =0, count=0, verf=0, max = 0;
	int max_bits=32;

    for(int i=0; i<max_bits ;i++)
    {
        bit = git_bit(N,i);
        if (bit == 1) 
        {
            if (flag == 0)
            {
                flag=1;
            }
            else if(flag == 1)
            {
                verf=1;
            }

            if (verf >0)
            {
                if (max<count)
                {
                    max = count;
                    verf = 0;
                    count = 0;
                }
                else
                {
                    verf = 0;
                    count = 0;
                }

            }
        }
        else if(flag==1)
        {
            count ++;
        }
    }

    return max;
}