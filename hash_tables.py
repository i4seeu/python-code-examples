## Problem 2: Find the first duplicate number
## lets use hash table to solve the problem the problem

def first_duplicate(arr):
    """Find the first duplicate number in an array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The first duplicate number if found; otherwise, -1.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

if __name__ == "__main__":
    # Example usage
    sample_array = [2, 1, 3, 5, 3, 2]
    result = first_duplicate(sample_array)
    if result != -1:
        print(f"First duplicate number is: {result}")
    else:
        print("No duplicate number found.")