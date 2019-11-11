def solution(progresses, speeds):
    answer = []
    days = 0
    idx = 0
    while True :
        days += 1
        count = 0
        #하루당 진행하는 일의 양
        for i in range(len(speeds)) :
            if progresses[i] < 100 :
                progresses[i] += speeds[i]
                
            if progresses[idx] >= 100 :
                count += 1
                idx += 1
            
        if count != 0 :
            answer.append(count)
        if sum(answer) == len(progresses) :
            break
        
    print(answer)
    return answer

solution([93,30,55],[1,30,5]) #[2,1]