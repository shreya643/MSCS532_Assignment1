def insertion_sort(arr):
    #loop over the array
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        #while loop to sort array in desc order
        while j >= 0 and key > arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [12, 40, 60, 22, 11, 13, 5, 6]
    print("Input:", arr)
    insertion_sort(arr)
    print("Output: ", arr)
    #adding another input
    arr1 = [1, 300, 45, 2, 19, 11, 20, 56]
    print("Input:", arr1)
    insertion_sort(arr1)
    print("Output: ", arr1)
