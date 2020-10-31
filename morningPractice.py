# “ Parens Valid
# Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 


def perensValid(var):
    state= True
    counter1= 0
    counter2= 0
    for i in range(0,len(var),1):
        print(var[i])
        if var[i] == "(":
            counter1 += 1
            print("counter1", counter1)
        if var[i] == ")" and counter1 > counter2:
            counter2 += 1
            print("counter2", counter2)
        elif var[i] == ")" and counter1 <= counter2:
            state = False
            return state
    if counter1 == counter2:
        state= True
    else:
        state= False
    print(counter1, counter2, state)


testStr="Y(3(p)p(3)r)s"
testStr1=")(()())"
testStr2="N(0)t )0(k"
perensValid(testStr)
x= perensValid(testStr1)
y= perensValid(testStr2)
print(x)
print(y)