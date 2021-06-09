def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)
    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1 

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append((n*m) / gcd(n, m))
    return answer