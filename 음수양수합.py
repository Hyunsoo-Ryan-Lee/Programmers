# <<음수양수 합>>

ab = [4,7,12]
sig = [True,False,True]

def solution(ab,sig):
    a = list(zip(ab,sig))
    ans = 0
    for i in a :
        if i[1] == True:
            ans += i[0]
        else:
            ans -= i[0] 
    return ans
print(solution(ab,sig))

def sol(a,b):
    return sum(a if b else -a for a,b in zip(a,b))
    
print(sol(ab,sig))