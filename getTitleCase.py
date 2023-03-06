
def getTitleCase(text):
    if text == "" or text == " ":
        return ""
    text = text.lower()
    titleCaseString = ""

    for i in range(len(text)):

        if i == 0 or not text[i-1].isalpha():
            titleCaseString += text[i].upper()
        else:
            titleCaseString += text[i]

    return titleCaseString




print(getTitleCase("!!!!!pepito@alwA!AAma!na"))

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'