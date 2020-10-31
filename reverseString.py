ourString = "Welcome to python"

def reverseString(string):
    newStr = ""
    for i in range(len(string)-1, -1, -1):
        newStr += string[i]
    return newStr

print(reverseString(ourString))

# arrays

x = [5,5,6,8,7,8]

for i in range(0, len(x), 1):
    print(x[i])