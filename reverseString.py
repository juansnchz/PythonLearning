def reverseString(text):
    if text == "" or text == " ":
        return ""
    lettersOfString = []
    reversedText = ""
    for letter in text:
        lettersOfString.append(letter)

    for i in range(-1, -(len(lettersOfString)+1),-1):
        reversedText += lettersOfString[i]
    print(reversedText)
    return reversedText


reverseString("Hello Mothafuckas")


assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'