# version 1 (open - close 이용하여)
'''
names = ['이예인','이현수','패숀의 정수','찬유의 볼살']

for i in names:
    print(f'안녕하세요 {i}님! 저입니다.')

for a in names:
    f = open(f'{a}.txt','w',encoding='utf-8')
    f.write(f'안녕하세요 저의 이름은 {a}입니다. 잘 부탁드립니다.')
    f.close()
'''

# version 2 (with open 이용하여)

# names = ['이예인','이현수','패숀의 정수','찬유의 볼살']
# for name in names:
#     with open(f'{name}.txt','w',encoding='utf8') as mail:
#         mail.write(f"""
#         안녕하세요! {name}님 편집자 이현수입니다.
#         {name}의 컨텐츠는 아주 인상깊게 잘 보고 있습니다.
#         앞으로도 잘 부탁드립니다.
#         """)



# 퀴즈2. 행맨 게임
'''
1. list에 3개 이상의 단어를 추가
2. list에서 random으로 하나의 단어를 선택
3. 단어의 길이에 맞게 밑줄 출력
4. 1글자씩 입력을 받되, 단어에 입력값 포함이면 correct, 틀리면 wrong 출력
5. 매번 입력 받을 때마다 맞힌 글자들 표시
'''
import random

# VERSION 1

#fruit = ['orange','banana','watermelon','strawberry','cherry','tomato', 'raspberry']
# select = random.choice(fruit) #banana
# under = list('_'*len(select)) # 아니면 언더바, 맞으면 알파벳, 아닌것만 언더바
# print(f'{len(fruit)}가지의 fruit 목록중 선택된 과일은 {len(select)} 단어입니다.')
# chance = 0
# wrong = 0
# while under.count('_') != 0:
#     word = input()
#     li = [a for a,b in enumerate(select) if b == word] #[1,3,5] / []
#     if len(li) > 0:
#         for j in li:
#             under[j] = word
#         chance += 1
#         print(''.join(under)+f' / 시도 횟수 : {chance} / 틀린 횟수 : {wrong}')
#     else:
#         chance += 1
#         wrong += 1
#         print(''.join(under)+f' / 시도 횟수 : {chance} / 틀린 횟수 : {wrong}')
# print()
# print(f'축하합니다! 정답은 \'{select}\' 입니다!')        


# VERSION 2

word = random.choice(fruit)
print("answer : "+word)
letters = ""

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w,end='')
        else:
            print('_',end='')
            succeed = False
    print()

    if succeed:
        print('Success')
        break

    letter = input("INPUT LETTER >>>")
    if letter not in letters:
        letters += letter

    print("Correct") if letter in word else print("Wrong")