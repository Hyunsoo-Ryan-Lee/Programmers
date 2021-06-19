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