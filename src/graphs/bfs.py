from collections import deque

def bfs(graph, start_node):
    """
    Explores the graph level by level starting from start_node.
    Returns a list of nodes in the order they were visited.
    """
    visited = set()
    queue = deque([start_node])
    visit_order = []

    visited.add(start_node)

    while queue:
        # Get the next node from the front of the queue (First-In-First-Out)
        current_node = queue.popleft()
        visit_order.append(current_node)

        # Look at neighbors using the method we wrote in graph.py
        neighbors = graph.get_neighbors(current_node)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visit_order