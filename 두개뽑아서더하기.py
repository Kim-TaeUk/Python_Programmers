def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    new_answer = []
    for k in answer:
        if k not in new_answer:
            new_answer.append(k)

    for i in range(len(new_answer)-1):
        for j in range(len(new_answer)-i-1):
            if new_answer[j] > new_answer[j+1]:
                new_answer[j+1], new_answer[j] = new_answer[j], new_answer[j+1]

    return new_answer