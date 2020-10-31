# “String: Is Palindrome
# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 

def reverseString(string):
    newStr = ""
    for i in range(len(string)-1, -1, -1):
        newStr += string[i]
    print(newStr)
    if newStr == string:
        newStr = True
        print("this is a palindrome")
        return newStr
    else:
        newStr = False
        print("this is not a palindrome")
        return newStr

str1="racecar"
str2="a x a"
str3="gottcha"

reverseString(str1)
reverseString(str2)
reverseString(str3)