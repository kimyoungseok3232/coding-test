# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    l = len(stones)
    val = min([max(stones[i:i+k]) for i in range(0,(l//k)*k,k)])
    
    loop_min = 0
    while 1:
        zero_stone, max_st_val = 0, 0
        for i in range(loop_min, l):
            if stones[i] <= val:
                if stones[i] > max_st_val: 
                    max_st_val, loop_min = stones[i], i
                zero_stone += 1
                if zero_stone == k: break
            else: zero_stone, max_st_val = 0, 0
        else: break
    
        val = max_st_val - 1
        
    return val+1