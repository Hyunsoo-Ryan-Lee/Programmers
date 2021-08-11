# 프로그래머스 - 구명보트

def solution(people, limit):
    people.sort(reverse=True)
    ans = 0
    for i in people:
        if i+people[-1] <= 100:
            ans += 1
            people.pop()
        else:
            ans += 1
    return ans

people = [20, 50, 50, 80]
limit = 100