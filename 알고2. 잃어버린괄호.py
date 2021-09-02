# 잃어버린 괄호

'''
>> 마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 주면 문제에서 원하는 답을 얻을 수 있다.

1. '-'를 기준으로 문자를 split 한다.

2. list에 저장된 문자들에 대해서도 '+'를 기준으로 split해서 덧셈 처리를 다 해준다.

3. 덧셈처리까지 다 된 숫자들이 list에 저장되면 첫째 항에서 나머지 항들의 합을 빼주면 된다.
'''

num = '55-50+40'
sp = num.split('-')
tot = [] 

for i in sp:
    pl = i.split('+')
    cnt = 0
    for j in pl:
        cnt += int(j)
    tot.append(cnt)

print(tot[0]-sum(tot[1:]))