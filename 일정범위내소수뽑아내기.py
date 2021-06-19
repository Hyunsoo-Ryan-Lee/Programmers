# Q1-1
# 반복문을 사용하여 임의의 값을 받아(2~9단) 구구단을 출력하는 프로그램을 작성하시오




# Q1-2
# 임의의 숫자의 범위를 정하고 (예: 0~100) 반복문을 사용하여 범위 내의 소수(素数)를 출력하는 프로그램을 작성하시오
# ※ 소수(素数): 1과 자기 자신만으로 나누어 떨어지는 정수

num = input('start : end => ') #5 10
rge = list(map(int,num.split(' ')))
total = []
for i in range(rge[0],rge[1]+1): # 5~10       
    ans = 0
    for j in range(2,(i//2)+1):
        if i%j == 0: ans += 1
    if ans == 0: total.append(i)
print(total)


# eve = []
# for i in range(10, 30):
#     for j in range(10, 30):
#         a = i * j
#         if str(a) == str(a)[::-1]:
#             eve.append(a)
# print(eve)
# print('*'*40)
# print(str(a)[::-1])



'''



'''


'''



