# 프로그래머스 정수삼각형

def solution(t):
    for i in range(1,len(t)): # 1,2,3
        for j in range(i+1): # 0,1 / 0,1,2 / 0,1,2,3
            if j == 0:
                t[i][j] += t[i-1][0]
            elif j == len(t[i])-1:
                t[i][j] += t[i-1][-1]
            else:
                t[i][j] += max(t[i-1][j-1], t[i-1][j])
    return max(t[len(t)-1])



t  =[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))

# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
