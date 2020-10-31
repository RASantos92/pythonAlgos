# “Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch  -  gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 
testStr=" there's no free lunch  -  gotta pay yer way. "
testStr1="Live from New York, it's Saturday Night!"
def acryonyms(var):
	newLst=''
	if var[0] != ' ':
		newLst += var[0]
	for i in range(1,len(var),1):
		if var[i-1] == ' ':
			newLst += var[i]
	return newLst.upper()

acryonyms(testStr)
acryonyms(testStr1)
x = acryonyms(testStr)
print(x)
