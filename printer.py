from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    priorities[location] = float(priorities[location])
    print(priorities)
    count = 1
    
    while True :
        if priorities[0] != max(priorities) :
            p = priorities.popleft()
            priorities.append(p)
        else : #첫 값이 가장 큰 값이면
            priorities.popleft()
            count += 1
        if type(priorities[0]) == float and priorities[0] == max(priorities) :
            answer = count
            break

    print(answer)
    return answer

solution([2,1,3,2],2)           #1
solution([1,1,9,1,1,1],0)       #5
solution([7,6,8,1,2,3,2,1],3)   #8