#include <math.h>

int solution(int A, int B, int K) {
    
    return (int)(floor(((double)B/K)) -  floor(((double)(A-1)/K)));
}