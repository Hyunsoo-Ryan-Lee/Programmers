'''
<삼각형> (17.39점 / 30점)

문제 설명
다음과 같은 숫자로 이루어진 삼각형이 있다.

74932
1325
457
92
1
가장 위의 행에 있는 숫자들을 제외하고, 각 숫자는 위와 오른쪽위에 있는 숫자의 합의 마지막 자리수이다.

tri에 숫자와 함께 알 수 없는 숫자 ? 가 주어 진다. (명확한 설명을 위해 예제 1을 참조하라). tri의 각 요소는 삼각형의 행을 의미하며 가장 위의 행부터 아래의 순서로 주어진다. 각 요소는 정확히 한자리 숫자만을 ('0' - '9') 포함하며 나머지 문자는 모두 '?'이다. 삼각형을 복원시켜 '?'가 없는 문자열 배열을 반환하여라.

참고 / 제약 사항
tri은 1개 이상, 50개 이하의 요소를 가진다.
(0을 기준으로) tri의 i번째 요소는 정확히 n-i개의 문자를 가진다. 이 때, n은 tri의 요소의 개수이다.
tri의 각 요소는 정확히 하나의 숫자만을 ('0'-'9') 가지며 나머지 문자는 모두 '?'이다.
테스트 케이스
tri = ["4??","?2","1"]리턴(정답): ["457","92","1"]
?를 변수로 바꿔보자. 4ab c2 1 이제 아래에서부터 위로 변수를 풀어보자. 먼저 (c + 2)의 마지막 자리수가 1이 되므로 c는 9이다: 4ab 92 1 이제 (4 + a)의 마지막 자리수가 9이므로 a는 5이다: 45b 92 1 마지막으로 (5 + b)의 마지막 자리수가 2이므로 b는 7이다.

tri = ["1"]리턴(정답): ["1"]
'''

class Solution:
    def solution(self, tri):
        if len(tri) == 1:
            return tri
        tri = tri[:][::-1]
        t_sep = []
        ans = []
        check = 0
        q_count = 0
        for i in tri:
            t_sep.append(list(i))
            q_count += i.count('?')
    
        while q_count != check:
            for i in range(len(t_sep)-1):
                for j in range(i+1):
                    arr = [t_sep[i][j], t_sep[i+1][j], t_sep[i+1][j+1]]
                    if arr.count('?') == 1:
                        if arr.index('?') == 0:
                            t_sep[i][j] = str((int(arr[1])+int(arr[2]))%10)
                            check += 1
                        elif arr.index('?') == 1:
                            t_sep[i+1][j] = str((int(arr[0])-int(arr[2]))%10)
                            check += 1
                        else:
                            t_sep[i+1][j+1] = str((int(arr[0])-int(arr[1]))%10)
                            check += 1
            if q_count == check:
                break
    
        for i in t_sep:
            ans.append(''.join(i))
        return ans[:][::-1]