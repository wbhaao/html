# 실패

def solution(bridge_length, weight, truck_weights):
    truck_list = [0]
    cnt = 0
    # 다리위에 트럭과 대기하고 있는 트럭이 하나라도 있다면
    while not (sum(truck_list) == 0 and len(truck_weights) == 0):
        # 트럭이 다리길이만큼 전진했나
        if len(truck_list) >= bridge_length:
            del truck_list[0]

        # 그러지 않았다면 한칸 전진
        if not (len(truck_weights) == 0):
            # 더 싦을 수 있다면
            if not (sum(truck_list)+truck_weights[0] > weight):
                # truck_weight[0] 삭제하고 append 
                truck_list.append(truck_weights.pop(0))
            else:
                truck_list.append(0)
            cnt += 1  
        else:
            return cnt + bridge_length
    return cnt

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
