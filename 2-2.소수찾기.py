# 소수 찾기

from itertools import permutations
def solution(number):
    ans = []
    for i in range(1,len(number)+1): #조합 개수
        for j in list(permutations(list(number),i)):
            ans.append(int(''.join(j)))
    ans = list(set(ans)) # 조합으로 만들 수 있는 수를 중복되지 않도록 ans에 담는다.
    # 여기서부턴 소수찾기 코드
    count = 0
    for num in ans:
        test = 0
        if num >= 2:
            for x in range(2,num//2+1):
                if num%x == 0:
                    test += 1
            if test == 0:
                count += 1  
    return count


a = '011'
print(solution(a))