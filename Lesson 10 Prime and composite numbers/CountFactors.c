#include <math.h>

int solution(int N) {
    
    int count = 0;
    int i = 1;

    while(pow(i, 2) < N)    // i*i will overflow
    {
        if(N%i == 0)
            {count+=2;}
        i += 1;
    }

    if(pow(i, 2) == N)
        {count += 1;}
	
    return count;
}