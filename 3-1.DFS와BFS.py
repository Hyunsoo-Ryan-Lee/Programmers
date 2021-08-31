# # 백준 - DFS와 BFS

# n=4
# p = [(1,2),(1,3),(1,4),(2,4),(3,4)]
# graph = [[0]*(n+1) for i in range(n+1)]
# visited = [0]*(n+1)
# for i in p:
#     graph[i[0]][i[1]] = 1
#     graph[i[1]][i[0]] = 1
# '''
# print(graph) -> 방문한 곳을 좌표형식으로 찍어서 행렬처럼 보이게 list에 저장

# graph = [[0, 0, 0, 0, 0], 
#          [0, 0, 1, 1, 1], 
#          [0, 1, 0, 0, 1], 
#          [0, 1, 0, 0, 1], 
#          [0, 1, 1, 1, 0]]

# visited = [0, 0, 0, 0, 0]
# '''

# def dfs(v):
#     visited[v] = 1 # 방문한 곳의 숫자를 1로 변경시킴
#     print(v, end='')
#     for i in range(1,n+1): # v를 기준으로 나머지 짝이 어떤 녀석인지 찾는다.
#         if visited[i] == 0 and graph[v][i]==1:
#             dfs(i) # 짝을 찾았으면 해당 숫자로 이동하여 다시 dfs 함수 반복.
# print(dfs(1))




# def solution(point,cnt,*line):
#     answer = []
#     now = 0
#     que = [1]
#     while len(que)>0:
#         answer.append(que[0])   # 왔다 갔다는 걸 넣어줌
#         now = que.pop(0)        # 현재 위치 지정
#         for i in line:
#             if i[0] == now and not i[1] in answer and not i[1] in que:  
#                 que.append(i[1])
#             elif i[1] == now and not i[0] in answer and not i[0] in que: 
#                 que.append(i[0])
#     answer = len(answer) - 1

#     return answer

# if __name__ == "__main__":
#     a = 7
#     b = 6
#     c = [1,2]
#     d = [2,3]
#     e = [1,5]
#     f = [5,2]
#     g = [5,6]
#     h = [4,7]
#     print(solution(a,b,c,d,e,f,g,h))


# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split(' '))))
n = 5
graph = [[1,2],[1,3],[1,4],[2,4],[3,4]]
visited = [True] + [False]*(n-1)
def dfs(v):
    visited[v] = True
    print(v,end='')
    for p in graph:
        if p[0] == v and visited[p[1]] == False:
            dfs(p[1])
    return ''
print(dfs(1))

ans = []
def bfs(v):
    visited = [True] + [False]*4
    visited[v] = True
    ans = [v]
    tot = []
    print(v,end='')
    while False in visited:
        for i in graph:
            if ans[0] == i[0] and visited[i[1]] == False:
                visited[i[1]] = True
                ans.append(i[1])
                tot.append(i[1])
                print(i[1],end='')
        ans.pop(0)
    return ''
print(bfs(1))