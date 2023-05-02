#include <math.h>

int solution(int N) {
    int i = (int) sqrt((double)N);

    for(;i>0;i--)
    {
        if(N%i == 0)
            {return (2 * (i + (N/i)));}
    }
    return 0;
}