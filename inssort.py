def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i
        
        # Shift elements greater than value to the right
        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1
        
        # Insert value at correct position
        array[j] = value
        print(f"\tAfter inserting element[{i}]={value}: {array}")

array = [5, 3, 1, 2, 6, 4]
print("Insertion sort...\nArray: ", array)
insertion_sort(array)
print("Final Array: ", array)