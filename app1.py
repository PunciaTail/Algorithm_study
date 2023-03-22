# 짝수의 합
# 제한사항 : 0 < n ≤ 1000

# 방법1
# def solution(n):
#     count = n  # n을 하나씩 빼가면서 돌리려고 count에 넣음
#     answer = 0

#     while 0 < count:
#         if count % 2 == 0:
#             answer += count
#         else:
#             pass
#         count -= 1

#     return answer


# 방법2
def solution(n):
    answer = 0

    for num in range(n+1):
        if num % 2 == 0:
            answer += num

    return answer
