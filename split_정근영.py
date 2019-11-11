def split_func(strings):
    tmp = []
    i_tmp = 'z'
    index_d = 0
    index_s = 0
    for  i in strings :
        if ord(i_tmp) < 65 and ord(i) >= 65 :
            tmp.append(strings[index_s:index_d])
            index_s = index_d
        i_tmp = i
        index_d += 1
    tmp.append(strings[index_d-1:])
    return tmp
    
strings = "abc123   5abc1 a123z" 
print(split_func(strings))