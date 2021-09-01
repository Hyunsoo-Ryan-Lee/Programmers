
# m = int(input())
# n = int(input())
# com = []
# for _ in range(n):
#     com.append(list(map(int, input().split(' '))))
n = 2
# com = [[1,2],[2,3],[1,5],[5,2],[5,6],[4,7]]
com = [[1,3],[2,3]]
visited = [True] + [False]*n
ans = []
def dfs(v):
    visited[v] = True
    ans.append(v)
    for i in com:
        if i[0] == v and visited[i[1]] == False:
            dfs(i[1])
    return len(ans)-1

print(dfs(1))