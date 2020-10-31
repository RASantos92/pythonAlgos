def sigma(num):
    if num <= 1:
        return 1
    else:
        return num + sigma(num-1)

def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num-1)


x = factorial(5)
print(x)

# 0,1,1,2,3,5,8,13,21,34,55
# 0 1 2 3 4 5 6 7   8  9 10
def rFib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return rFib(num - 1) + rFib(num - 2)



# print(rFib(9))

def fabb(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fabb(num - 1) + fabb(num - 2)

# y = fabb(8)
# print(y)

def rGCF(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return rGCF(num1 - num2, num2)
    elif num1 < num2:
        return rGCF(num1, num2 - num1)

def gcf(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == num2:
        return num1
    if num1 > num2:
        if num1 % num2 == 0:
            return num2
        else:
            return gcf(num1-num2, num2)
    if num1 < num2:
        if num2 % num1 == 0:
            return num1
        else:
            return gcf(num1, num2-num1)

x= rGCF(21,18)
print(x)

y= gcf(100, 250)

print("jerrys", y)\



# “ String: In-Order Subsets
# Create strSubsets(str). Return an array with every possible in-order character subset of str. The resultant array itself need not be in any specific order – it is the subset of letters in each string that must be in the same order as they were in the original string. Given "abc", return an array that includes ["", "c", "b", "bc", "a", "ac", "ab", "abc"] (in any order).”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 

# from collections import deque


# # Recursive function to print all distinct subsets of S
# # S   --> input set
# # out --> list to store subset
# # i   --> index of next element in set S to be processed
# def findPowerSet(S, out, i):

# 	# if all elements are processed, print the current subset
# 	if i < 0:
# 		print(list(out))
# 		return
# 	# include current element in the current subset and recur
# 	out.append(S[i])
# 	findPowerSet(S, out, i - 1)
# 	# exclude current element in the current subset
# 	out.pop()	   # backtrack
# 	# remove adjacent duplicate elements
# 	while i > 0 and S[i] == S[i - 1]:
# 		i = i - 1

# 	# exclude current element in the current subset and recur
# 	findPowerSet(S, out, i - 1)

# # Program to generate all distinct subsets of given set
# if __name__ == '__main__':

# 	S = ["p","y","th","o","n"]

# 	# sort the set
# 	# S.sort()

# 	# create an empty list to store elements of a subset
# 	out = deque()
# 	findPowerSet(S, out, len(S) - 1)

def ios(string, sub = "", i=0):
    if i == len(string):
        return [sub]
    else:
        return ios(string, sub + string[i], i+1) + ios(string, sub, i+1)

print(ios("abc"))

