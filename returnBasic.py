#return statement
def multiply(a=99,b=55):
    return a*b

print(multiply(99,55))
result= multiply(80,10)
print(result)
#write a function square (num) that returns the square of a number.
def square(num):
    return num**2
print(square(99))
#write a function that takes a string and returns the count of vowels and consonants separately.
def func(userInput):
    #define vowels
    vowels="aeiouAEIOU"
    countVowel=0
    countConsonants=0
    #Annie1559
    for eachcharacter in userInput:
        if(eachcharacter.isalpha()):
            if(eachcharacter in vowels):
                countVowel=countVowel+1
            else:
                countConsonants+=1
    return countVowel,countConsonants

#function call
vowels, consonants =func(" Priyanka Priyadarshini Muduli")
print(vowels, consonants)

#string uppercase karna
def convert_to_upper(word):
    return word.upper()
print(convert_to_upper("Annie"))
#creat a  function full_name(fname ,iname)that returns the full name joined with a space.
def full_name (fname ,iname):
    return fname +""+iname
print(full_name("Annie","Thakur"))
