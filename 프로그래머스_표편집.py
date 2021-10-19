'''
https://programmers.co.kr/learn/courses/30/lessons/81303
'''

def solution(n, k, cmd):
    delete = []
    cmd_list = list(range(n))
    current = k
    for i in cmd:
        if i[0] == 'D':
            current += int(i[-1])
        elif i[0] == 'U':
            current -= int(i[-1])
        elif i[0] == 'C':
            if cmd_list[current] == cmd_list[-1]:
                loc = cmd_list.pop(current)
                delete.append([current,loc])
                current -= 1
            else:
                loc = cmd_list.pop(current)
                delete.append([current,loc])
        else:
            if delete[-1][1] < cmd_list[k]:
                cmd_list.insert(delete[-1][0], delete[-1][1])
                delete.pop()
                current += 1
            else:
                cmd_list.insert(delete[-1][0], delete[-1][1])
                delete.pop()
    ans = ''
    for i in list(range(n)):
        if i in cmd_list:
            ans += 'O'
        else:
            ans += 'X'
    return ans

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8,2,cmd))


# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# if cmd[0][0] == 'D':
#     print('dd')

# print(int(cmd[0][-1]))