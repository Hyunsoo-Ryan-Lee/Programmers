# 팩토리얼 진법 (백준)
'''
팩토리얼 진법에서는 i번 자리의 값을 ai×i!로 계산한다.
즉, 팩토리얼 진법에서 719는 10진법에서 53과 같다.
그 이유는 7×3! + 1×2! + 9×1! = 53이기 때문이다.

팩토리얼 진법으로 작성한 숫자가 주어졌을 때,
10진법으로 읽은 값을 구하는 프로그램을 작성하시오. 
'''

# 답은 맞지만 runtime error
from abc import abstractproperty
from math import factorial

n = 719
a = list(map(int,str(n)))
a.append(0)
a.reverse()
ans = 0
for i in a:
    ans += (i*factorial(a.index(i)))
print(ans)



# 비밀 지도 - 비트 연산자 사용!

import re
def solution(n, arr1, arr2):
    a1 = [0]*n
    for i in range(n):
        a1[i] = re.sub('1','#',(bin(arr1[i] | arr2[i])[2:]).zfill(n)) 
        # 연산중 자리수가 줄어들 수 있으므로 zfill을 사용해서 자리수를 맞춰준다!!
        a1[i] = re.sub('0',' ',a1[i])
    return a1


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))
