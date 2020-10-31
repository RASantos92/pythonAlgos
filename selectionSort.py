testLst=[89,65,4,57,2,15,4,8,75]

def selectionSort(lst):
    for j in range(len(lst)-1):
        min = j
        print("j is :", lst[j])
        for i in range(j+ 1,len(lst)):
            if lst[i] < lst[min]:
                min = i
                print("min has value of :", min, "lst :", lst[min])
        lst[j], lst[min] = lst[min], lst[j]
        print(lst)

selectionSort(testLst)