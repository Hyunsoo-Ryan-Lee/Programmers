# 프로그래머스 - N으로 표현

# def solution(n,number):
#     p_set = [0,[n]]
#     if n == number:
#         return 1
#     for i in range(2,9):
#         tot = []
#         tot.append(int(str(n)*i))
#         for j in range(i):
#             tot.append(j+n)
#             tot.append(abs(j-n))
#             tot.append(j*n)
#             if j!=0:
#                 tot.append(j/n)
#         p_set.append(tot)
#         if number in tot:
#             return i
#     if not number in tot:
#         return -1

def solution(n,number):
    if n == number:
        return 1
    p_set = [set() for i in range(8)]
    for i in range(len(p_set)):
        p_set[i].add(int(str(n)*(i+1)))
        # 5  55  555  5555  55555  555555  5555555  55555555
    for i in range(1,8): # 마지막 index는 최종 수행 결과로 만들어지는거기 때문에 1~7까지만 연산
        for j in range(i):
            for op1 in p_set[j]:
                for op2 in p_set[i-j-1]:
                    p_set[i].add(op1+op2)
                    p_set[i].add(abs(op1-op2))
                    p_set[i].add(op1*op2)
                    if op2 != 0:
                        p_set[i].add(op1//op2)
        if number in p_set[i]:
            return i+1
    
    return -1                   
    
print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)

