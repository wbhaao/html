# 실패

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    truck_list = deque([0] * bridge_length)
    bridge_weights = 0
    cnt = 0
    # 다리위에 트럭과 대기하고 있는 트럭이 하나라도 있다면
    while True:
        bridge_weights -= truck_list.popleft()
        # 준비하고 있는 트럭이 있다면

        if truck_weights:
            # 더 싦을 수 있다면
            if not (bridge_weights+truck_weights[0] > weight):
                # truck_weight[0] 삭제하고 append 
                truck_list.append(truck_weights.popleft())
                bridge_weights += truck_list[-1]
            else:
                truck_list.append(0)
            
        # 준비중인 트럭이 없다면
        else:
            return cnt + bridge_length
        cnt += 1  
print(solution(2, 10, [7,4,5,6]))

def solution(bridge_length, weight, truck_weights):
    #추상화: 남은 트럭들 중 넣을 수 있는 타이밍 잡기
    #계획: 1. [0,0,0,0,0,0,0] -> [1:]+([0] or [truck_weights[0]] 
    # 2. del truck_weights[0] 
    # 3. truck_weights의 길이가 0이면 종료  
    answer = 0
    bridge = [0]*bridge_length
    
    # 이 식 뭔가 나랑 비슷함
    while not (len(truck_weights) == 0 and sum(bridge) == 0):
        answer += 1
        # 이거 왜하는 걸까? // 마지막에 bridge가 뒤에서 추가될거라
        del bridge[0]
        nextNum = 0
        # truck_weights가 있다면
        if truck_weights: 
            # 싦을 트럭을 포함해 weight 보다 적거나 같다면
            if sum(bridge) + truck_weights[0] <= weight:
                # nextNum은 다리에 추가될 트럭 // 맨 앞에 있는
                nextNum = truck_weights[0]
                # 준비되있던 트럭 삭제
                del truck_weights[0]
        bridge.append(nextNum)
        
#     return answer
