# 팩토리얼 진법 (백준)
'''
팩토리얼 진법에서는 i번 자리의 값을 ai×i!로 계산한다.
즉, 팩토리얼 진법에서 719는 10진법에서 53과 같다.
그 이유는 7×3! + 1×2! + 9×1! = 53이기 때문이다.

팩토리얼 진법으로 작성한 숫자가 주어졌을 때,
10진법으로 읽은 값을 구하는 프로그램을 작성하시오. 
'''

# 답은 맞지만 runtime error

# from math import factorial

# n = 719
# a = list(map(int,str(n)))
# a.append(0)
# a.reverse()
# ans = 0
# for i in a:
#     ans += (i*factorial(a.index(i)))
# print(ans)
