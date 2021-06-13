def solution(n):
    add = 0
    new = str(n)
    for i in range(len(new)):
        add += int(new[i])    
    return add