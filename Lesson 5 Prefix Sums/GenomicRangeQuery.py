def solution(S, P, Q):
    result = []
    for i in range(len(P)):
        if 'A' in S[P[i]: Q[i] + 1]:
            result.append(1)
        elif 'C' in S[P[i]: Q[i] + 1]:
            result.append(2)
        elif 'G' in S[P[i]: Q[i] + 1]:
            result.append(3)
        elif 'T' in S[P[i]: Q[i] + 1]:
            result.append(4)
    return result
	
def solution2(S, P, Q):
    d =dict()
    d = {'A':1,'C':2,'G':3,'T':4}
    min = []

    for i in range(len(P)):
        sum = float('inf')
        for j in d:
            if j in S[P[i] : Q[i]+1 ]:
                min.append(d[j])
                break
    return min