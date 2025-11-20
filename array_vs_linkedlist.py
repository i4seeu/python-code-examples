'''
In this file, we compare the performance of array-based lists and linked lists
for searching operations. We implement a binary search algorithm for the array-based list
and a linear search algorithm for the linked list. We then measure and compare the time taken
by each method to find an element in a large dataset.
'''
import time
import random 
class Node:
    """A node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    """A simple linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def linear_search(self, item) -> int:
        """Perform linear search to find the index of the item in the linked list.

        Args:
            item: The element to search for in the linked list.

        Returns:
            int: The index of the item if found; otherwise, -1.
        """
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1
    
# Sample sorted array for binary search
NAMES = [
    "Laura",
    "Lauren",
    "Leah",
    "Mackenzie",
    "Madison",
    "Manuel",
    "Marc",
    "Marcus"]

# Create a linked list and populate it with the same names
linked_list = LinkedList()
for name in NAMES:
    linked_list.append(name)

def binary_search(arr, item) -> int:
    """Perform binary search on a sorted array to find the index of the item.

    Args:
        arr (list): A sorted list of elements.
        item: The element to search for in the list.

    Returns:
        int: The index of the item if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        if mid_value == item:
            return mid
        elif mid_value < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Choose a random name to search for
    target_name = random.choice(NAMES)

    # Measure time for binary search on array
    start_time = time.time()
    index_array = binary_search(NAMES, target_name)
    end_time = time.time()
    print(f"Binary Search: Found '{target_name}' at index {index_array} in array in {end_time - start_time:.10f} seconds.")

    # Measure time for linear search on linked list
    start_time = time.time()
    index_linked_list = linked_list.linear_search(target_name)
    end_time = time.time()
    print(f"Linear Search: Found '{target_name}' at index {index_linked_list} in linked list in {end_time - start_time:.10f} seconds.")