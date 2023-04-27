def solution(H):
    if len(H) == 1:
        return 1

    stones = 1
    hights = [H[0]]

    for i in range(1, len(H)):
        if H[i] < H[i-1]:
            while(len(hights)>0 and H[i]<hights[-1]):
                hights.pop()

            if(len(hights)==0 or H[i]!=hights[-1]):
                stones += 1
                hights.append(H[i])

        elif H[i] > H[i-1]:
            stones += 1
            hights.append(H[i])

    return stones