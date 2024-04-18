def selection_Sort(arr):
    for i in range(len(arr)-1):  # array starts from 0 so subtract 1 to get length of the array
        minn = i  # loop for the minimum value
        for j in range(i + 1, len(arr)):  # loop the remaining unsorted array elements
            if arr[j] < arr[minn]:  # if an element is less than the minimum(minn) replace the minimum
                minn = j  # put minimum to array j place
        x = array[i]  # swap the element with the minimum output element
        array[i] = array[minn]  # new unsorted array value into array i place
        array[minn] = x  # put x into the minimum of the array
    return arr  # return sorted array


array = [4, 1, 6, 2, 5, -1, 7, 3, 8, 10, 9, 0]
selection_Sort(array)

print(array)
