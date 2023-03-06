def mergeTwoLists(list1, list2):
    sortedlist = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            sortedlist.append(list1[i1])
            i1 += 1


        elif list1[i1] > list2[i2]:
            sortedlist.append(list2[i2])
            i2 += 1

        elif list1[i1] == list2[i2]:
            sortedlist.append(list1[i1])
            sortedlist.append(list2[i2])
            i1 +=1
            i2 +=1


    if len(list1) > i1:
        for i in range(i1, len(list1)):
            sortedlist.append(list1[i])

    if len(list2) > i2:
        for i in range(i2, len(list2)):
            sortedlist.append(list2[i])
    return sortedlist



assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]


