def rot13(text):
    encrypted_text = ""
    for i in range(0,len(text)):
        if not text[i].isalpha():
            encrypted_text += text[i]
        else:
            unicode = ord(text[i]) + 13
            if text[i].isupper() and unicode>90:
                unicode -= 26

            if text[i].islower() and unicode>122:
                unicode -= 26

            encrypted_text += chr(unicode)



    return encrypted_text





assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'