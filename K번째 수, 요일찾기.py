
# <<K번째 수>>

'''
1. 1~20까지 숫자가 순서 없이 들어가있는 list 형태의 배열 A가 있습니다.
[a,b,c] 형태로 배열이 주어질 때 a번째~b번째 수까지 뽑아서 역순정렬하고 
그 역순정렬한 list에서 c번째에 해당하는 값을 뽑아내는 함수를 만드세요.


A = [17,12,8,3,18,11,15,13,1,6,7,4,20,14,19,2,5,10,9,16]

def numbers(a,b,c):
    x = A[a:b+1]
    x.sort(reverse=True)
    return x[c]

print(numbers(3,8,2))
'''

# <<요일 찾기>>
'''
2. 2021년 1월1일은 금요일입니다. [a,b] 형태로 값을 받아서 
2021년 a월 b일의 요일값을 반환하는 함수를 만드세요.(윤년아님)

day = [31,28,31,30,31,30,31,31,30,31,30,31]
today = ["목","금","토","일","월","화","수"]

def date(a,b):
    p=0
    for i in range(a):
        p+=(day[i])
    return today[(p-31+b)%7]

print(date(5,18))
'''


from collections import deque
bridge = deque([1]*2)
print(sum(bridge))