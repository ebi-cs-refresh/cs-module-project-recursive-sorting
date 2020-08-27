# TO-DO: complete the helper function below to merge 2 sorted arrays

arr1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 40]
arr2 = []


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements  # * its this part that is not clicking
    merged_arr = []
    # Your code here

    # starting at the beginning of a and b
    # compare the next value of each other
    # add smallest merged arr

    leftindex = 0
    rightindex = 0
    l = len(arrA)
    r = len(arrB)

    while leftindex < l and rightindex < r:
        # global count
        # count += 1
        if arrA[leftindex] < arrB[rightindex]:
            merged_arr.append(arrA[leftindex])
            leftindex += 1
        else:
            merged_arr.append(arrB[rightindex])
            rightindex += 1
    merged_arr += arrA[leftindex:]+arrB[rightindex:]

    # return merged_arr+arrA[leftindex:]+arrB[rightindex:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return arr
    else:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        return merge(merge_sort(left_arr), merge_sort(right_arr))

    return arr


print(merge_sort(arr2))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     pass
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     pass
#     # Your code here
