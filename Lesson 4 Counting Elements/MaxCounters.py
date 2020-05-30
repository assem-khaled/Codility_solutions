def solution(N, A):
    if N ==0:
        return []
    counters = [0] * N
    max_ = 0
    all_max = 0
    for i in A:
        if i-1 <len(counters):
            if all_max > counters[i-1]:
                counters[i-1] = all_max
            counters[i-1] +=1
            if counters[i-1] > max_:
                max_ = counters[i-1]
        else:
            all_max = max_
    counters = [max(all_max, i) for i in counters ]

    return counters