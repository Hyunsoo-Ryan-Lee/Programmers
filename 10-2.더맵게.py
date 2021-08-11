# <<더 맵게>>

def solution(s,k):
    ans = 0
    while min(s) < k:
        try:
            s.sort()
            s[0] += s[1]*2
            s.pop(1)
            ans += 1
            if s[0] >= k : break
        except IndexError:
            return -1
    return ans
s = [1, 2, 3, 9, 10, 12]
k = 105
print(solution(s,k))
