# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            print(f" first iteration {j}")
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                print(f" set smallest {j}")
    # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
        print(f"set temp {temp}")
    return arr


selection_sort([5, 9, 4, 3, 6, 7])
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# Traverse through all array elements

# Driver code to test above


bubble_sort([1, 2, 4, 3, 9, 7])
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
