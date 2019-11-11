def solution(skill, skill_trees):
    answer = 0
    for strk in skill_trees:
        temp = ""       # 스킬에 없는 스킬들은 지우고 저장할 변수
        isOk = True     # 가능한 스킬트리의 개수를 저장할 변수

        # 1. 스킬에 없는 스킬들은 뺴고 temp에 저장
        for s in strk:
            if skill.find(s) != -1:
                temp += s

        # 2. temp의  길이만큼 스킬과 비교하여
        # 같으면 가능한 스킬트리, 다르면 불가능한 스킬트리
        for i in range(len(temp)):
            if skill[i] != temp[i]:
                isOk = False
                break

        # 3. 가능한 스킬트리라면 정답 개수를 1 증가
        print(temp,isOk)
        if isOk == True:
            answer += 1

    print(answer)
    return answer

solution('CBD',['BACDE','CBADF','AECB','BDA'])  #2