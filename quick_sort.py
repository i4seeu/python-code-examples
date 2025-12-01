# lets implement a quick sort algorithm in python
def quick_sort(arr):
    """Sort an array using the quick sort algorithm.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
if __name__ == "__main__":
    # Example usage
    sample_array = [3,6,8,10,1,2,1]
    sorted_array = quick_sort(sample_array)
    print("Original array:", sample_array)
    print("Sorted array:", sorted_array)