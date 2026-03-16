def dfs(graph, start_node):
    """
    Explores the graph as deeply as possible along each branch.
    Returns a list of nodes in the order they were visited.
    """
    visited = set()
    stack = [start_node]
    visit_order = []

    while stack:
        # Get the most recently added node (Last-In-First-Out)
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            visit_order.append(current_node)
            
            # Get neighbors and add them to the stack
            neighbors = graph.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return visit_order