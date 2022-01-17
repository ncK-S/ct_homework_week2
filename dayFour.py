# Q1: Create a function that returns the sum of the two lowest 
# positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    number=numbers 
    number.sort(reverse=True)
    a=number.pop()
    b=number.pop()
    return a+b

print(sum_two_smallest_numbers([4,3,2,1]))

# count positive sum negative
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += x
    return [pos, neg]