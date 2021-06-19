# <<소수 만들기>>

# from itertools import*  -> combinations 함수 사용!
# combinations(리스트, 뽑는 갯수)



from itertools import*
def solution(a):
    b = list(combinations(a,3))
    c = []
    for i in b:
        c.append(sum(i))
    total = 0
    for i in c:
        ans = 0
        for j in range(1,i+1):
            if i%j == 0:
                ans += 1
        if ans == 2:
            total += 1
    return total