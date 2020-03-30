"""
https://app.codility.com/demo/results/training69PH2A-3R8/

Lesson5 - PassingCars

최적화 버전이 아니라 개인적인 풀이
최적화 답은 : https://www.martinkysel.com/codility-passingcars-solution/
"""

"""
1. 0이 나오기 전 1을 무효로 처리하기 위해 east T/F 사용
2. 연속된 0이 나오는 경우 체크를 위한 bef_car와 east_cnt
"""

def solution(A):
    cross = [[0,0]] # index 오류를 피하기 위한 초깃값
    car_cnt=0
    east_cnt = 1
    east=False
    bef_car=-1
    res = 0

    for idx, car in enumerate(A):
        if car == 0:
            east=True
            if bef_car == 0:
                east_cnt+=1
            if car_cnt > 0:
                cross.append([car_cnt, east_cnt])
                car_cnt=0
                east_cnt=1
        else:
            if east:
                car_cnt+=1
        bef_car=car
    
    # 마지막 value 처리
    if car_cnt > 0:
        cross.append([car_cnt, east_cnt])

    # 계산식    
    passed = sum([i[0] for i in cross])
    for idx, (cars, cnt) in enumerate(cross[1:],1):
        passed-= cross[idx-1][0]
        res+=passed*cnt
        if res > 1000000000:
            return -1
    return res

"""
계산식 설명
[0,1,0,0,1,1,0,1,1]
cross => [[0,0],[1,1],[2,2],[2,1]]

첫번째 0은 3 두번째와 세번째 0은 각각 2
5 X 1 + 4 X 2 + 2 X 1= 15
앞의 car_cnt를 빼면서 더함
5 X 1 + (5 - 1) X 2 + (5 - 1 - 2) X 1 = 15
"""