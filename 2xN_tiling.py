def solution(n):
    answer = 0

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        answer_list = [0,1,2]
        for i in range(3, n+2):
            answer_list.append((answer_list[i-1] + answer_list[i-2])% 1000000007)
        return answer_list[i-1]
        
    print(answer)
    return answer

solution(4)     #5
solution(2)     #2
solution(3)     #3
solution(5)     #8