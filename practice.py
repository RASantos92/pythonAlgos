testStr = "AAAABBBBCCCCAAABBB"
testStr1 = 'ABBCcAD'
testArr = [1,2,2,3,3]

def uniqueInOrder(iterable):
    newArr = []
    for i in range(0,len(iterable)-1,1):
        if i == len(iterable)-2:
            newArr += iterable[i]
        if iterable[i] != iterable[i+1]:
            # newArr += i
            newArr += iterable[i]
    return newArr

x = uniqueInOrder(testStr)
y = uniqueInOrder(testStr1)
# z = uniqueInOrder(testArr)
print(x)
print(y)
# print(z)