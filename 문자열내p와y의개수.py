def solution(s):
    str = []
    str = list(s)
    count_p = 0
    count_y = 0
    for i in range(len(str)):
        if str[i] == 'p' or str[i] == 'P':
            count_p += 1
        elif str[i] == 'y' or str[i] == 'Y':
            count_y += 1
        else:
            pass
    if count_p == count_y:
        return True
    else:
        return False