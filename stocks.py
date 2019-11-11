def solution(prices):
    answer = []
    for i in range(len(prices)) :
        count = 0
        for j in range(i+1,len(prices)) :
            count += 1
            if prices[j] < prices[i] :
                break
        answer.append(count)

    print(answer)
    return answer

solution([1,2,3,2,3])	#[4,3,1,1,0]