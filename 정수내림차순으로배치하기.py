# def solution(n):   
#     m = str(n)
#     string = ""
#     list_n = []
#     list_m = []
#     list_n = list(m)
#     for x in list_n:
#         list_m.append(int(x))
#     list_m.sort(reverse = False)
#     for y in list_m:
#         string = str(y)+string
#     return int(string)
def solution(n):
    n = list(str(n))
    n.sort(reverse = True)

    answer = 0
    answer = int("".join(n))
    
    return answer