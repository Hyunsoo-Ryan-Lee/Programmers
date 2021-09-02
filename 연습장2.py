


def solution(tic):
    start = {}
    # 아주 wow한 방법. dictionary의 get method 사용!
    for i in tic:
        start[i[0]] = start.get(i[0],[]) + [i[1]]
        # ['a']+['b'] = ['a', 'b']
    for i in start:
        start[i].sort(reverse = True)
    ans = ['ICN']

    while len(ans) != len(tic)+1:
        ans.append(start[ans[-1]].pop())    

    return ans


tic = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

# print(solution(tic))


def solution(tickets):
    routes = dict()
    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  

    for r in routes.keys():
        routes[r].sort(reverse=True)

    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top].pop())
            # routes[top] = routes[top][:-1]
    
    answer = path[::-1]
    return answer

tic = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

print(solution(tic))

