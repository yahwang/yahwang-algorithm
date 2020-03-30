
"""
Lesson 1 - BinaryGap
https://app.codility.com/demo/results/trainingR7QZR5-Y9N/
"""

def solution(N):
    bit_list = []
    num = N
    while True:
        if num == 1:
            bit_list.insert(0,num)
            break
        else:
            bit_list.insert(0,num % 2)
            num = num // 2
    
    gap_cnt = 0
    is_gap = False
    res = 0
    for bit in bit_list:
        if is_gap:
            if bit == 0:
                gap_cnt+=1
            else:
                res = max(gap_cnt,res)
                gap_cnt = 0
        else:
            if bit == 1:
                is_gap=True
    return res