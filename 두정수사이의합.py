def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        for i in range(a, b+1):
            answer += i
    else:
        a, b = b, a
        for i in range(a, b+1):
            answer += i
    return answer