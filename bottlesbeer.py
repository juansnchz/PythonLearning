def bottlesBeer(bottles):
    i = bottles
    while i > 2:
        print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,")
        print("Take one down, \nPass it around")
        print(f"{i-1} bottles of beer on the wall\n")
        i = i-1
    if i == 2:
        print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,")
        print("Take one down, \nPass it around")
        print(f"{i - 1} bottle of beer on the wall\n")
        i = i-1
    if i == 1:
        print(f"{i} bottle of beer on the wall,\n{i} bottle of beer,")
        print("Take one down, \nPass it around")
        print("No more bottles of beer on the wall\n")



bottlesBeer(80)