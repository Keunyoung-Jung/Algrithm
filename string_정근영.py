def my_len(s) :
    count = 0
    for i in s :
        count += 1
    return count

def my_find(s,word):
    if word in s :
        for i in range(my_len(s)) :
            if word == s[i:i+my_len(word)] :
                index = i
                return index
    else :
        return '\'{}\' is not found!'.format(word)
        
def my_split(s,word =' '):
    ret = []
    sett = 0
    for i in range(my_len(s)) :
        if word == s[i] :
            ret.append(s[sett:i])
            sett = i+1
            
    ret.append(s[sett:])
    return ret
        
string8 = 'Hello wo'
string11 = 'He.lo w.rld'
find_word = 'lo'
find_word2 = 'kk'
split_src = '.'

print('\'{}\' \tlength\t\t :'.format(string8),my_len(string8))
print('\'{}\' \tlength\t\t :'.format(string11),my_len(string11))
print('\'{0}\' \tfind \'{1}\' start index :'.format(string8,find_word),my_find(string8,find_word))
print('\'{0}\' \tfind \'{1}\' start index :'.format(string11,find_word2),my_find(string11,find_word2))
print('\'{}\' \tsplit Default\t :'.format(string8),my_split(string8))
print('\'{0}\' \tsplit \'{1}\'\t :'.format(string11,split_src),my_split(string11,split_src))
print('\'{}\' \tsplit Default\t :'.format(string11),my_split(string11))
