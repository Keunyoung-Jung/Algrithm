dataSet = ["A","B","C","D"]
subSet = []

def makeCandidate(dataSet):
    mCand = []
    for i in range(len(dataSet)):
        for j in range(i+1, len(dataSet)):
            set1 = set(dataSet[i]).union(set(dataSet[j]))
            if len(set1) > len(dataSet[i]) + 1:
                continue
            list1 = list(set1)
            list1.sort()
            if tuple(list1) not in mCand:
                mCand.append(tuple(list1))
    return mCand   

tempSet = dataSet
for i in range(1,len(dataSet)):        
    tempSet = makeCandidate(tempSet)
    subSet.append(tempSet)
    
print(subSet)    