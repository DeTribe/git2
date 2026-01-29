def merge_sort(array):
   if len(array) > 1:
      Middle=int(len(array)//2)
      left = array[:Middle]
      right = array[Middle:]
      print("\tSplit to ", left, right)

      #Recursivley sort both halves
      merge_sort(left)
      merge_sort(right)
      #Algorithm to be written here

      i=j=0
      for element in range(len(array)):
          L = left[i] if i < len(left) else None
          R = right[j] if j < len(right) else None
          if ((L is not None and R is not None)and (L < R))or R is None:
             array[element] = L
             i += 1
          elif ((L is not None and R is not None) and (L >= R)) or L is None:
             array[element] = R
             j += 1
      print("\t\tMerging: " , left, right)     
     
array=[5,3,1,2,6,4]
print("Merge sort...\nArray: " , array)
merge_sort(array)
print("Array: ", array)
