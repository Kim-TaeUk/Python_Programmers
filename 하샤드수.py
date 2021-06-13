def solution(x):
    new = str(x)
    add = 0
    for i in range(len(new)):
        add += int(new[i])

    if x % add == 0:
        return True
    else:
        return False