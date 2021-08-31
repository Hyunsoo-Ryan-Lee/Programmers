
def bfs(p,v):
    n = 8
    visited = [True]+[False]*n
    start = [v]
    ans = [v]
    visited[start[0]]=True
    p.sort()
    while False in visited:
        for i in p:
            if i[0] == start[0] and visited[i[1]] == False:
                start.append(i[1])
                visited[i[1]] = True
                ans.append(i[1])
        start.pop(0)
    return ans


visited = [True]+[False]*8
p = [(1,3),(1,8),(1,2),(2,7),(3,4),(3,5),(4,5),(7,6),(7,8)]
p.sort()
ans = []
def dfs(v):
    visited[v] = True
    ans.append(v)
    for i in p:
        if i[0] == v and visited[i[1]] == False:
            dfs(i[1])
    return ans


# print(bfs(p,1))
# print(dfs(1))


graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*9
ans = []
def dfs1(v):
    visited[v] = True
    ans.append(v)
    for i in graph[v]:
        if visited[i] == False:
            dfs1(i)
    return ans
print(dfs1(1))

def bfs1(v):
    visit = [True] + [False]*8
    com = [v]
    ans = [v]
    visit[v] = True
    while False in visit:
        for i in graph[com[0]]:
            if visit[i] == False:
                ans.append(i)
                com.append(i)
                visit[i] = True
        com.pop(0)
    return ans
print(bfs1(2))

