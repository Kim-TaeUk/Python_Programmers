def is_prime_number(a):
    for b in range(2, a):
        if a % b == 0:
            return False
    return True

def solution(nums):
    answer = 0
    add = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                add.append(nums[i] + nums[j] + nums[k])

    for x in range(len(add)):
        if is_prime_number(add[x]) == True:
            answer += 1
    return answer
#  EunSeo's HELP! Jun 14,2021
#  Woosung's HELP! Jun 14,2021