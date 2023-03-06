import random

def generatePassword(length:int):
    password = []
    LOWERCASE = list("abcdefghijklmnopqrstuvwxyz")
    UPPERCASE = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    NUMS = list("1234567890")
    SPECIAL_CHARS = list("~!@#$%^&*()_+")
    ALL = LOWERCASE + UPPERCASE + NUMS + SPECIAL_CHARS
    if length < 12:
        length = 12
    password.append(LOWERCASE[random.randint(0,len(LOWERCASE))-1])
    password.append(UPPERCASE[random.randint(0, len(UPPERCASE)-1)])
    password.append(NUMS[random.randint(0, len(NUMS)-1)])
    password.append(SPECIAL_CHARS[random.randint(0, len(SPECIAL_CHARS)-1)])
    while len(password) <length:
        password.append(ALL[random.randint(0, len(ALL) - 1)])
    random.shuffle(password)
    return "".join(password)


print(generatePassword(1))




