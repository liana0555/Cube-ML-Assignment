def dfs_search(start_state, max_depth=7):
    # Checking to avoid re-checking
    visited = set()
    stack = [(start_state, [], 0)]

    while stack:
        current, path, depth = stack.pop()

        if current in visited or depth > max_depth:
            continue
        visited.add(current)


        if current.is_solved():
            return path + [current]
        for neighbor in current.get_neighbors():
            stack.append((neighbor, path + [current], depth + 1))
    return None
