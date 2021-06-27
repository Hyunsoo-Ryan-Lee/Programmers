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
