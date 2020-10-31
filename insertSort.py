testLst=[1,9,6,5,7,8,65]

def insertSort(lst):
    for j in range(len(lst)-1):
        hold = j
        print("j idx", j, "j value", lst[j])
        for i in range(j,-1,-1):
            if lst[hold] < lst[i]:
                lst[i], lst[hold] = lst[hold], lst[i]
            print(lst,"i", lst[i],"hold", lst[hold])

insertSort(testLst)