# astar.py
import heapq
import itertools

def heuristic(state):
    count = 0
    for face in state.faces.values():
        if len(set(face)) > 1:
            count += 1
    return count

def astar_search(start_state):
    visited = set()
    heap = []
    counter = itertools.count()
    heapq.heappush(heap, (heuristic(start_state), 0, next(counter), start_state, []))

    while heap:
        est_total, cost, _, current, path = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current.is_solved():
            return path + [current]

        for neighbor in current.get_neighbors():
            new_cost = cost + 1
            est = new_cost + heuristic(neighbor)
            heapq.heappush(heap, (est, new_cost, next(counter), neighbor, path + [current]))

    return None
