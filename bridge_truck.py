def solution(bridge_length, weight, truck_weights):
    answer = 0
    out = []
    ing = []
    time_stamp = []
    isRunning = True
    while (isRunning):
        if len(truck_weights) == 0 and len(ing) == 0:
            #대기열도 다리위도 다빠져나갔을때
            answer = sum(time_stamp)
            isRunning == false
        if sum(ing) == 0 :                      
            # 다리에 트럭이 없을때
            ing.append(truck_weights.pop(0))
            time_stamp.append([0])
        elif (weight-sum(ing)) >= truck_weights[0] and sum(truck_weights)>0 :
            #다리 남은 무게가 남을때랑 남은트럭이있을때.
            ing.append(truck_weights.pop(0))
            time_stamp+1
            time_stamp.append([0])
        elif  (weight-sum(ing)) <= truck_weights[0] :
            #다리에 차가있지만 더들어가지못할때
            time_stamp = time_stamp+1

    print(answer)
    return answer

solution(2,10,[7,4,5,6])    #8
solution(100,10,[10])       #101
solution(100,100,[10,10,10,10,10,10,10,10,10,10])   #110