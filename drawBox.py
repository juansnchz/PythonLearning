def drawBox(size:int):
    if size <1:
        return
    print(" "*(size+1)+"+"+"-"*(size*2)+"+")
    for i in range(size):
        print(" "*(size-i)+"/"+" "*size*2+"/"+" "*i+"|")
    print("+"+"-"*size*2+"+"+" "*size+"+")
    for j in range(size, 0, -1):
        print("|"+" "*size*2+"|"+" "*(j-1)+"/")
    print("+"+"-"*size*2+"+")


for i in range(1, 6):
    drawBox(i)