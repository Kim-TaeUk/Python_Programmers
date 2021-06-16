def solution(n):
    new = []
    new = list(str(n))
    new.reverse()
    answer = []
    for i in range(len(new)):
        answer.append(int(new[i]))
    return answer