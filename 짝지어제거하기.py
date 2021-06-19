# <<짝지어 제거하기>>

def solution(a):
    ans = []
    for i in a:
        if len(ans) == 0 :
            ans.append(i)
        elif i != ans[-1]:
            ans.append(i)
        else:
            ans.pop()
    if len(ans) == 0: return 1
    else: return 0

a = 'baabaa'
print(solution(a))