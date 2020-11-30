# Python program for counting sort
# which takes negative numbers as well

# The function that sorts the given arr[]


def count_sort(lst):
    max_element = int(max(lst))
    min_element = int(min(lst))

    # compute range of elements
    k = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0

    count = [0 for i in range(k)]
    output = [0 for i in range(len(lst))]

    # Store count of each character
    for i in range(len(arr)):
        count[lst[i] - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array

    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_element] - 1] = arr[i]
        count[arr[i] - min_element] -= 1

    return output


# Driver program to test above function
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
ans = count_sort(arr)
print("Sorted character array is " + str(ans))
