def selection_sort (array):
    for index in range (0, len(array)-1 ):
        value = array[index]
        current = index

  # Algorithm to execute goes here

        for element in range( index+1, len(array)):
            if array[element] < array[current]:
                current = element

        if current != index:
            array[index] = array[current]
            array[current] = value


        print('\tResolving Element[', index, '] to ', array)

array = [5,3,1,2,6,4]
print('\nSelection sort...\narray: ', array)

selection_sort(array)
print('Array: ', array)
   