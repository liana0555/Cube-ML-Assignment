# bfs.py
from collections import deque

def bfs_search(start_state, max_depth=7):
    visited = set()
    queue = deque([(start_state, [], 0)])  # (текущее состояние, путь, глубина)

    while queue:
        current, path, depth = queue.popleft()
        if current in visited or depth > max_depth:
            continue
        visited.add(current)

        if current.is_solved():
            return path + [current]

        for neighbor in current.get_neighbors():
            queue.append((neighbor, path + [current], depth + 1))

    return None
