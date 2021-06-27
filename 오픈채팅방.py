# <<오픈채팅방>>

'''
record의 각 항을 빈칸 단위로 split하여 새로운 list에 담아준다.
{고유 ID : 이름} 이렇게 매치되는 dictionary를 만들어준다.
1) Leave 일때는 그냥 나가니깐 나간다는 메세지만 append 해주면 된다.
2) Enter 일때는 고유 id 값을 비교하여 바뀐 이름으로 dict에 저장 후 들어왔다는 메세지 append
3) change 일때는 고유 id 값 비교 후 dict에 바뀐 이름으로 저장.
4) id와 메시지가 append된 곳의 각 항들을 이제 출력해주면 되는데 만들어진 dict를 이용하여
id key를 name value로 바꿔서 메세지와 함께 출력.
'''

def solution(record):
    ans = []
    log = []
    match = {}
    for a in record:
        b = a.split(' ')
        if b[0] == 'Leave': log.append([b[1],'님이 나가셨습니다.'])
        elif b[0] == 'Enter':
            match[b[1]] = b[2]
            log.append([b[1],'님이 들어왔습니다.'])
        elif b[0] == 'Change':
            match[b[1]] = b[2]
    for c in log:
        ans.append(match[c[0]] + c[1])
    return ans

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",\
    "Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))