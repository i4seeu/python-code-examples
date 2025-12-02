## lets design a breadth first search algorithm in python
from collections import deque
class Node:
    """A node in a graph."""

    def __init__(self, value):
        self.value = value
        self.adjacents = []

    def add_edge(self, neighbor):
        """Add an edge from this node to a neighbor node."""
        self.adjacents.append(neighbor)

def breadth_first_search(start_node, target_value):
    """Perform a breadth-first search to find a target value in the graph.

    Args:
        start_node (Node): The node to start the search from.
        target_value: The value to search for.

    Returns:
        Node: The node containing the target value if found; otherwise, None.
    """
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node.value == target_value:
            return current_node
        visited.add(current_node)

        for neighbor in current_node.adjacents:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return None

if __name__ == "__main__":
    # Example usage
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")

    node_a.add_edge(node_b)
    node_a.add_edge(node_c)
    node_b.add_edge(node_d)
    node_c.add_edge(node_e)

    target = "E"
    print(node_a)
    result_node = breadth_first_search(node_a, target)
    if result_node:
        print(f"Node with value '{target}' found.")
    else:
        print(f"Node with value '{target}' not found.")