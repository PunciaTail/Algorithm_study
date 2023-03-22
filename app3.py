# 암호 해독
# 제한사항
# 1 ≤ cipher의 길이 ≤ 1,000
# 1 ≤ code ≤ cipher의 길이
# cipher는 소문자와 공백으로만 구성되어 있습니다.
# 공백도 하나의 문자로 취급합니다.

def solution(cipher, code):
    answer = ''
    for idx, value in enumerate(cipher):
        if (idx+1) % code == 0:
            answer += value
        else:
            pass
    return answer
