def solution(heights):
    answer = []
    sign = 0
    for i in range(len(heights)-1,-1,-1) :
        sw = 0
        for j in range(i,-1,-1) :
            if heights[j] > heights[i] :
                answer.insert(0,j+1)
                sw = 1
                break
        if sw == 0 :
            answer.insert(0,0)
    
    print(answer)
    return answer

solution([6,9,5,7,4])       #[0,0,2,2,4]
solution([3,9,9,3,5,7,2])   #[0,0,0,3,3,3,6]
solution([1,5,3,6,7,6,5])   #[0,0,2,0,0,5,6]