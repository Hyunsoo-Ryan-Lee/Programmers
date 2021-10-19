def solution(rows, columns, queries):
    table = []
    for i in range(rows):
        table.append(list(range(columns*i+1,columns*(i+1)+1)))

    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
        table[query[0]][query[1]+1] = tmp
        
        # answer.append(small)
        return table
qu = [[2,2,5,4]]
print(solution(6,6,qu))
        