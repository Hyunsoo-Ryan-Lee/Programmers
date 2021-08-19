# a = [3,2,1]
# print(list(enumerate(a)))


def solution(x,y):
    if x == 0 and y ==0:
        return "Possible"
    sx = 0
    for i in range(18,-1,-1):
        if x >= 3**i:
            sx = i
            break

    ans = []
    while x > 0:
        for i in range(sx+1,-1,-1):
            if x >= 3**i:
                ans.append(i)
                break
        x -= 3**i

    sy = 0
    for i in range(18,-1,-1):
        if y >= 3**i:
            sy = i
            break

    while y > 0:
        for i in range(sy+1,-1,-1):
            if y >= 3**i:
                ans.append(i)
                break
        y -= 3**i
    ans.sort()
    if ans == list(range(max(sx,sy)+1)):
        return 'Possible'
    else:
        return 'Impossible'



print(solution(3,10))
