def bubbleSort(list:list):
    for i in range(len(list)-1):
        for j in range(i,len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


    return list
print(bubbleSort([8, 2, 9, 6, 3]))

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]