# 프로그래머스 괄호 변환

# 괄호 2개의 쌍이 같은 최초의 index 반환 함수
def div(str):
    left = 0
    right = 0
    good = []
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            good.append('(')
        else:
            right += 1
            if len(good) != 0:
                good.pop()
        if left == right:
            return i+1

# 솔루션 함수
def solution(p):
    if len(p) == 0:
        return p

    ind = div(p)
    u = p[:ind]
    v = p[ind:]
    if u.startswith('('):
        return u + solution(v)

    ans = '(' + solution(v) + ')'
    for j in u[1:-1]:
        if j == '(':
            ans += ')' 
        else:
            ans += '('
    return ans

p = '()))((()'
print(solution(p))


