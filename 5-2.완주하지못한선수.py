#완주하지 못한 선수

#풀이 1
from collections import Counter
import collections
def solution(p,c):
    co = Counter(p)-Counter(c)
    return list(co.elements())[0]

p = ["leo", "kiki", "eden"]	
c = ["eden", "kiki"]
print(solution(p,c))


#풀이 2
def solution2(p,c):
    ans = ""
    p.sort()
    c.sort()
    for i in range(len(c)):
        if p[i] != c[i]:
            ans = p[i]
            break
    return p[-1] if ans=="" else ans
        
    
a = ["marina", "josipa", "nikola", "vinko", "filipa"]
b = ["josipa", "filipa", "marina", "nikola"]
print(solution2(a,b))
print(sorted(a))
