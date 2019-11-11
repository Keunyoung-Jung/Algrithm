import random

num_arr = [0,1,2,3,4,5,6,7,8,9]

def user_input ():
    sw = 1 
    while sw :
        new_in = []
        user_in = input('4자리의 숫자를 입력해 주세요(중복숫자 불가) : ')
        for i in range(4):
            new_in.append(int(user_in[i]))
        for i in range(4):
            for j in range(i+1,4-i) :
                if new_in[i] == new_in[j] :
                    print('중복이 존재 합니다 다시 입력해 주세요.')
                    break
                else :
                    sw = 0
                    break
    return(new_in)

def chk_BS(arr,user):
    b_count = 0
    s_count = 0
    for i in range(4):
        for j in range(4) :
            if user[i] == arr[j] :
                if i == j :
                    s_count+=1
                else :
                    b_count+=1
    return s_count,b_count

k = []
for i in range(0,4) :
    if i == 0 :
        k.append(num_arr.pop(random.randint(1,len(num_arr)-1)))
    else :
        k.append(num_arr.pop(random.randint(0,len(num_arr)-1)))
        
print(k)
count = 0
while True :
    count +=1
    user = user_input()
    s_count,b_count = chk_BS(k,user)
    
    if s_count == 4 :
        print('homerun!!  byebye')
        break
    else :
        print('{0}Strike!! and {1}Ball..'.format(s_count,b_count))