testLst=[9,8,7,5,4,6,2,3,1]
print(testLst)
def bubbleSort(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1]= lst[i+1], lst[i]
    return lst

bubbleSort(testLst)
print(testLst)