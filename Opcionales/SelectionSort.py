def selectionSort(arr):
    # find the length of the list
    len_newarr = len(arr)
    # loop through the values
    for i in range(len_newarr):
        # for each pass of the loop set the index of the minimum value
        min_index = i
        # compare the current value with all the remaining values in the array
        for j in range(i+1,len_newarr):
            # to update the min_index if we found a smaller int
            if arr[j] < arr[min_index]:
                min_index = j
        # if the index of the minimum value has changed
        # we will make a swap
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr

print(selectionSort([23,4,12,1,31,14]))
