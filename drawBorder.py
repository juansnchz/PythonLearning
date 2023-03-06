def drawBorder(width:int, height:int):
    if width >= 2 and height >= 2:
        print("+"+"-"*(width-2)+"+")
        for i in range(1, height-1):
            print("|"+" "*(width-2)+"|")

        print("+" + "-" * (width - 2) + "+")
    else:
        return None



drawBorder(2,2)

