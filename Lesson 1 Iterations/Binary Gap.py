def solution(N):
    s = str(bin(N)[2:])
    s = s.strip('0')
    s = s.split('1')
    return len(max(s))