def drawRectangle(width,height):
    if width <=0 or height<=0:
        return None
    for j in range(height):
        for i in range(width):
            print("#", end="")
        print()


drawRectangle(10,4)
drawRectangle(0,0)