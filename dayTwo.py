#with list write function to return list of numbers < 10
a = [1, 11, 2, 3, 51, 8, 13, 8, 34, 5, 89]

for i in a:

    if i < 10:

        print(i)







# 2 write function that takes two lists and returns them merged and sorted

list1 = [1, 45, 23, 22, 8, 17, 28, 40]
list2 = [36, 41, 3, 9, 50, 22, 10, 39]

def linear_merge(list1, list2):
    result = []

    while list1 and list2:
        result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))

    return (result + list1 + list2)[-1::-1]