def count_duplicates(arr:list):
    duplicates = {}
    for item in arr:
        duplicates[item]= arr.count(item)
    return duplicates

def mostFrequentNumber(dict:dict):
    frequentNumber = None
    mostFrequentNumberCount = 0

    for key, value in dict.items():
        if dict[key]>mostFrequentNumberCount:
            frequentNumber = key
            mostFrequentNumberCount = dict[key]
    print(f"The most frequent number in the dictionary is {frequentNumber} and it appears {mostFrequentNumberCount} times")




fruits = [1,1,1,1,1,1,1,1,2,4,5,4,3,2,1,6,7,8,9,33,2,1,2,1,42,1,1,2,3,2,2,2,2,2,2,2,2]

print(count_duplicates(fruits))
mostFrequentNumber(count_duplicates(fruits))

