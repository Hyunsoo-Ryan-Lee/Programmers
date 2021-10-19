#프로그래머스 - 튜플
'''
https://programmers.co.kr/learn/courses/30/lessons/64065
'''

def solution(s):
    fir = s[2:-2].split('},{')
    if len(fir) == 1:
        return list(map(int,fir))
    sec = []
    for i in fir:
        sec.append(list(map(int,i.split(','))))
    sec.sort(key=lambda x:len(x))
    ans = sec[0]
    for i in range(1,len(sec)):
        ans.extend(list(set(sec[i])-set(sec[i-1])))
    return ans
        

    
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
