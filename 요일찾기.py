# <<요일 찾기>>
'''
2. 2021년 1월1일은 금요일입니다. [a,b] 형태로 값을 받아서 
2021년 a월 b일의 요일값을 반환하는 함수를 만드세요.(윤년아님)
'''
day = [31,28,31,30,31,30,31,31,30,31,30,31]
today = ["목","금","토","일","월","화","수"]

def date(a,b):
    p=0
    for i in range(a):
        p+=(day[i])
    return today[(p-31+b)%7]

print(date(5,18))