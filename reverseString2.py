function reverseString(string){
    var newString="";
    for(var i=string.length -1; i>=0; i--){
        newString += string[i];
    }
    console.log(newString);
    return newString;
}

var testString="this is my string";
var x= reverseString(testString);
console.log(x);