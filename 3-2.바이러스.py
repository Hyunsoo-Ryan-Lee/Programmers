
# m = int(input())
# n = int(input())
# com = []
# for _ in range(n):
#     com.append(list(map(int, input().split(' '))))
# com = [[1,3],[2,3]]

# def bfs(com, v):
#     com.sort()
#     visited = [False]*n
#     node = [v]
#     ans = [v]
#     cnt = 1
#     visited[v-1]= True
#     while False in visited:
#         for i in com:
#             if i[0] == node[0] and visited[i[1]-1] == False:
#                 visited[i[1]-1] = True
#                 node.append(i[1])
#                 ans.append(i[1])
#         node.pop(0)

#         if len(node) == 0:
#             cnt += 1

#     return ans, cnt
    
# n = 7
# com = [[1,2],[2,3],[1,5],[5,2],[5,6],[4,7]]

# print(bfs(com,1))




# def bbb(n, com):
#     visited = [True] + [False]*n
#     que = []
#     ans = []
#     cnt = 0
#     com.sort()
#     while False in visited:
#         no = visited.index(False)
#         que.append(no)
#         ans.append(no)
#         visited[no] = True
#         while que:
#             current = que.pop(0)
#             for (a,b) in com:
#                 if current == a and visited[b] == False:
#                     que.append(b)
#                     ans.append(b)
#                     visited[b] = True
#                     cnt += 1
#     return cnt
# n = 3
# com = [[1,2],[2,3],[1,5],[5,2],[5,6],[4,7]]
# com = [[1,3],[2,3]] 
# print(bbb(n, com))

n = 3
matrix = [[0]*(n+1) for _ in range(n+1)]
com = [[1,3],[2,3]]

for i in com:
    matrix[i[0]][i[1]] = 1
    matrix[i[1]][i[0]] = 1

def bfs(start):
    que = [start]
    ans = [start]
    while que:
        current = que.pop()
        for i in range(len(matrix[current])):
            if matrix[current][i] and i not in ans:
                ans.append(i)
                que.append(i)
    return len(ans)
print(bfs(1))


n = 3
matrix = [[0]*(n+1) for _ in range(n+1)]
com = [[1,3],[2,3]]
visited = [True] + [False]*n
for i in com:
    matrix[i[0]][i[1]] = 1
    matrix[i[1]][i[0]] = 1
ans = []
'''
[0, 0, 0, 0]
[0, 0, 0, 1]
[0, 0, 0, 1]
[0, 1, 1, 0]
'''
def dfs(v):
    visited[v] = True  # [1,0,0,0] -> [1,1,0,0] -> [1,1,0,1] -> [1,1,1,1]
    for i in range(1,n+1):
        if matrix[v][i] == 1 and visited[i] == False:
            ans.append(i) # 3 , 2
            dfs(i) # 3 , 2
    return ans
print(dfs(1))
    