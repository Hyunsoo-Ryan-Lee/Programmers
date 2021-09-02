# N = int(input())
# S = [list(map(int, input().split())) for _ in range(N)]

# n = 6 
# s = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
r = list(range(n))
from itertools import combinations

team = list(combinations(r,3))
t_1 = team[:int(len(team)/2)]
t_2 = team[int(len(team)/2):][::-1]
# print(t_1)
# print(t_2)
tot_1 = []
tot_2 = []
for i in t_1:
    p = list(combinations(i,2))
    tot = 0
    for (a,b) in p:
        tot += s[a][b]
        tot += s[b][a]
    tot_1.append(tot)

for i in t_2:
    p = list(combinations(i,2))
    tot = 0
    for (a,b) in p:
        tot += s[a][b]
        tot += s[b][a]
    tot_2.append(tot)

ans = []
for i in range(len(tot_1)):
    ans.append(abs(tot_1[i]-tot_2[i]))

print(ans)
print(tot_1)
print(tot_2)