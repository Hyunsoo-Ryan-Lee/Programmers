# 모의고사
'''
def solution(ans):
    x = [1,2,3,4,5]
    y = [2,1,2,3,2,4,2,5]
    z = [3,3,1,1,2,2,4,4,5,5]
    p = [0,0,0]
    total = []
    for i in range(len(ans)):
        if x[i%5] == ans[i]:
            p[0] += 1
        if y[i%8] == ans[i]:
            p[1] += 1
        if z[i%10] == ans[i]:
            p[2] += 1
    
    return p

ans = [1,3,2,4,2]
print(solution(ans))
'''

# 소수 찾기
'''
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
'''


# 숫자카드 (백준 알고리즘)


# n = int(input())
# a = list(map(int,input().split(' ')))
# m = int(input())
# b = list(map(int,input().split(' ')))
# ans = []
# for i in m:
#     ans.append(n.count(i))
# ans = list(map(str,ans))
# print(' '.join(ans))



from collections import Counter

# print(Counter('is this the real life'))
# Counter({' ': 4, 'i': 3, 'e': 3, 's': 2, 't': 2, 'h': 2, 'l': 2, 'r': 1, 'a': 1, 'f': 1})
n = int(input())
a = list(map(int,input().split(' ')))
m = int(input())
b = list(map(int,input().split(' ')))
card = Counter(a) # 요 구문을 for문의 print안에 넣어버리면 시간 초과가 됨.
for i in b:
    print(card[i],end=' ')
