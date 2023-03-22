# 대문자와 소문자
# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 영어 대문자와 소문자로만 구성되어 있습니다.


def solution(my_string):
    answer = ''
    for word in my_string:
        # 소문자면 대문자, 대문자면 소문자
        if word.isupper():
            answer += word.lower()
        else:
            answer += word.upper()
    return answer
