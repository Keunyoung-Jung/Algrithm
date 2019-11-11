def solution(n):
    answer = ''
    while 0<n:
        n-=1
        if n%3 == 0 :    
            answer = '1' + answer 
            n//=3
        elif n%3 == 1:
            answer = '2' + answer
            n//=3
        else:
            answer = '4' + answer
            n//=3

    print(answer)
    return answer


solution(1)
solution(76)
solution(3)
solution(346)
solution(9)