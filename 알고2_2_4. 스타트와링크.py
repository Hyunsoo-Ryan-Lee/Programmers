from itertools import combinations


# n = 6
# com = [[0, 1, 2, 3, 4, 5],
# [1, 0, 2, 3, 4, 5],
# [1, 2, 0, 3, 4, 5],
# [1, 2, 3, 0, 4, 5],
# [1, 2, 3, 4, 0, 5],
# [1, 2, 3, 4, 5, 0]]
n = 4
com = [[0, 1, 2, 3],
[4, 0, 5, 6],
[7, 1, 0, 2],
[3, 4, 5, 0]]


a = list(range(1,n+1))
tot = list(combinations(a,int(n/2)))
fir = tot[:int(len(tot)/2)]
sec = tot[int(len(tot)/2):][::-1]
one = []
two = []
ans = []

for a in fir:
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a)):
            cnt += com[a[i]-1][a[j]-1]
    one.append(cnt)

for a in sec:
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a)):
            cnt += com[a[i]-1][a[j]-1]
    two.append(cnt)

for p in range(len(one)):
    ans.append(abs(one[p]-two[p]))
print(min(ans))

