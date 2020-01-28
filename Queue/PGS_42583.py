"""
deque의 maxlen을 활용한 문제

0을 밀어넣어 트럭의 이동을 표현
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = [0 for _ in range(10001)]
    queue = deque([0] * bridge_length, maxlen=bridge_length)
    passed_left = len(truck_weights)
    bridge_weight = 0
    while passed_left != 0:
        # 시간 경과 후 처리
        is_truck = queue.pop()
        if is_truck != 0:
            passed_left -= 1
            bridge_weight -= is_truck
        # 트럭이 건너는 처리
        if truck_weights:
            # 무게 제한
            if truck_weights[0] + bridge_weight > weight:
                queue.appendleft(0)
            else:
                truck = truck_weights.pop(0)
                queue.appendleft(truck)
                bridge_weight += truck
        else:
            queue.appendleft(0)

        answer += 1

    return answer
