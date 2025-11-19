"""Sorted names array for examples and tests.

This module provides a single list `NAMES` containing 128 first names
in alphabetical order.
"""

NAMES = [
	"Aaliyah",
	"Aaron",
	"Abigail",
	"Adam",
	"Addison",
	"Adrian",
	"Adriana",
	"Aiden",
	"Alan",
	"Albert",
	"Alex",
	"Alexander",
	"Alexandra",
	"Alexis",
	"Alice",
	"Alicia",
	"Barbara",
	"Barry",
	"Benjamin",
	"Bethany",
	"Bianca",
	"Blake",
	"Brandon",
	"Brenda",
	"Brian",
	"Brianna",
	"Caleb",
	"Cameron",
	"Cara",
	"Carl",
	"Carlos",
	"Carol",
	"Caroline",
	"Casey",
	"Cassandra",
	"Catherine",
	"Charles",
	"Charlotte",
	"Daisy",
	"Dakota",
	"Dale",
	"Daniel",
	"Daniela",
	"Danielle",
	"David",
	"Dawn",
	"Deborah",
	"Eddie",
	"Edith",
	"Eleanor",
	"Elena",
	"Eli",
	"Elias",
	"Elijah",
	"Elizabeth",
	"Fiona",
	"Floyd",
	"Frances",
	"Francis",
	"Frank",
	"Frederick",
	"Gabrielle",
	"Gail",
	"Garrett",
	"Gary",
	"Gavin",
	"Gemma",
	"George",
	"Hannah",
	"Harold",
	"Harry",
	"Hazel",
	"Heather",
	"Henry",
	"Holly",
	"Ian",
	"Ibrahim",
	"Isaac",
	"Isabel",
	"Isabella",
	"Jack",
	"Jackson",
	"Jacob",
	"Jade",
	"Jake",
	"James",
	"Jamie",
	"Jane",
	"Janet",
	"Jared",
	"Jason",
	"Jasper",
	"Karen",
	"Karla",
	"Katherine",
	"Kathleen",
	"Kayla",
	"Keith",
	"Lacey",
	"Lance",
	"Larry",
	"Laura",
	"Lauren",
	"Leah",
	"Mackenzie",
	"Madison",
	"Manuel",
	"Marc",
	"Marcus",
	"Maria",
	"Marie",
	"Mark",
	"Nancy",
	"Natalie",
	"Nathan",
	"Oliver",
	"Olivia",
	"Omar",
	"Pamela",
	"Parker",
	"Patricia",
	"Patrick",
	"Quinn",
	"Rachel",
	"Rafael",
	"Ralph",
	"Samantha",
	"Samuel",
]



## lets do a birnary search tree implementation here

def binary_search_tree(arr, item) -> int:
    """Perform binary search on a sorted array to find the index of the item.

    Args:
        arr (list): A sorted list of elements.
        item: The element to search for in the list.

    Returns:
        int: The index of the item if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        count += 1
        print(f"Iteration {count}: left={left}, right={right}, mid={mid}, mid_value={mid_value}")  
        if mid_value == item:
            return mid
        elif mid_value < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Example usage
    name_to_find = "Samuel"
    index = binary_search_tree(NAMES, name_to_find)
    if index != -1:
        print(f"{name_to_find} found at index {index}.")
    else:
        print(f"{name_to_find} not found in the list.")