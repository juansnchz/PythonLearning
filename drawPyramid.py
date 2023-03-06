def drawPyramid(height: int):
    empty_space = (height*2-1)//2
    hashtag = 1
    for i in range(height):
        print(" "*empty_space+"#"*(hashtag)+" "*empty_space)
        empty_space -= 1
        hashtag += 2

drawPyramid(50)


