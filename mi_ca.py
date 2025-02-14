from collections import deque

# Define the initial state (left missionaries, left cannibals, boat position)
initial_state = (3, 3, 1)  # (M_left, C_left, Boat_position) -> Boat is on the left side, all on the right side

# Define the goal state (all on the left side)
goal_state = (0, 0, 0)  # (M_left, C_left, Boat_position) -> Boat is on the left side, all on the left side

# Possible boat moves (Missionaries, Cannibals)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    """Check if the state is valid (missionaries never outnumbered)"""
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    # If missionaries are outnumbered on either side, it's an invalid state
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False  # Out of bounds
    return True

def bfs():
    """Breadth-First Search to find the shortest solution"""
    queue = deque([(initial_state, [])])  # (state, path)
    visited = set()

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) == goal_state:
            path.append((m_left, c_left, boat))
            print("Solution found:")
            for step in path:
                print(step)
            print(f"Total steps: {len(path) - 1}")
            return

        if (m_left, c_left, boat) in visited:
            continue
        visited.add((m_left, c_left, boat))

        for m_move, c_move in moves:
            if boat == 1:  # Boat on the left
                new_state = (m_left - m_move, c_left - c_move, 0)
            else:  # Boat on the right
                new_state = (m_left + m_move, c_left + c_move, 1)

            if is_valid(new_state):
                queue.append((new_state, path + [(m_left, c_left, boat)]))

    print("No solution found")

# Run the solver
bfs()
