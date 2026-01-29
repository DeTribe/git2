def merge_sort(array, depth=0):
    """Simple version with hierarchical output"""
    indent = "    " * depth
    
    if len(array) > 1:
        print(f"{indent}Splitting {array}")
        
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
        # Recursive calls
        merge_sort(left, depth + 1)
        merge_sort(right, depth + 1)
        
        # Merge
        i = j = 0
        for k in range(len(array)):
            L = left[i] if i < len(left) else None
            R = right[j] if j < len(right) else None
            
            if ((L is not None and R is not None) and (L < R)) or R is None:
                array[k] = L
                i += 1
            elif ((L is not None and R is not None) and (L >= R)) or L is None:
                array[k] = R
                j += 1
        
        print(f"{indent}Merging {left} + {right} → {array}")
    
    return array

# Run it
array = [5, 3, 1, 2, 6, 4]
print("Merge sort...")
print(f"Original: {array}")
merge_sort(array, depth=1)  # Start at depth 1
print(f"Sorted: {array}")

