int gcd(int a, int b)
{
    if (a % b ==0)
    {
        return b;
    }
    else 
	{
        gcd(b, a%b);
    }
}
int solution(int N, int M) {
    
    return N / gcd(N,M);
}