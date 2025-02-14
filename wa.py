from collections import deque

def water_jug_solver(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0, [])])  # (jug1_state, jug2_state, path)

    while queue:
        x, y, path = queue.popleft()
        
        # If we reach the target amount in jug1
        if y == target or x == target:
            path.append((x, y))
            print("Steps to reach the solution:")
            for step in path:
                print(step)
            print(f"Total steps: {len(path) - 1}")
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Possible next states with recorded paths
        next_states = [
            (jug1, y, path + [(x, y)]),  # Fill jug1
            (x, jug2, path + [(x, y)]),  # Fill jug2
            (0, y, path + [(x, y)]),  # Empty jug1
            (x, 0, path + [(x, y)]),  # Empty jug2
            (max(0, x - (jug2 - y)), min(jug2, y + x), path + [(x, y)]),  # Pour jug1 -> jug2
            (min(jug1, x + y), max(0, y - (jug1 - x)), path + [(x, y)])   # Pour jug2 -> jug1
        ]

        for state in next_states:
            queue.append(state)

    print("No solution")

# Solve for 4-gallon and 3-gallon jugs to get 2 gallons in the 4-gallon jug
j1 = int(input("Enter the capacity of Jug 1: "))
j2 = int(input("Enter the capacity of Jug 2: "))
c = int(input("Enter the amount of water to be measured: "))
water_jug_solver(j1, j2, c)