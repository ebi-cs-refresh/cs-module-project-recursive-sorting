
arr1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 40]
arr2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):

    print(start, end)

    if end is None:
        end = len(arr)-1
    if start > end:
        return False
    mid = (start+end)//2
    print("target", target, arr[mid])

    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

    # if len(arr) == 0:
    #     print("Array is empty")
    #     return -1
    # else:
    #     mid = start + (end-start)//2
    #     print("start, end", start, end)
    #     if start > end:
    #         return False
    #     print("mid", arr[mid], target)
    #     if arr[0] == target:
    #         return True
    #     if arr[len(arr)-1] == target:
    #         return True
    #     print('is arr biger than target', arr[mid] == target, arr[mid], target)
    #     if arr[mid] == target:
    #         return True
    #     else:
    #         if target < arr[mid]:
    #             return binary_search(arr, target, start, mid-1)
    #         if target >= arr[mid]:
    #             return binary_search(arr, target, mid+1, end)
    #         else:
    #             print("wayy")


# print(binary_search(arr1, -8, 0, len(arr1)-1), 1)
print(binary_search(arr1, 44, 0, len(arr1)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == target:
            return True
        else:
            if target < arr[mid]:
                agnostic_binary_search(arr[:mid], target)
            else:
                agnostic_binary_search(arr[mid+1], target)
    return target


print(agnostic_binary_search(arr1, 2))
