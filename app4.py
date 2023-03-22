# 양꼬치
# 제한사항
# 0 < n < 1,000
# n / 10 ≤ k < 1,000
# 서비스로 받은 음료수는 모두 마십니다.

def solution(n, k):
    answer = 0
    count = 0  # 음료수 빼야할 개수
    print(n, k)
    if n >= 10:
        count = n // 10
        k -= count
    else:
        pass
    answer = (n*12000) + (k*2000)
    return answer
