class State():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        # Initial state of the problem
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

    def is_goal(self):
        # Goal is when all missionaries and cannibals are on the right side
        return self.cannibalLeft == 0 and self.missionaryLeft == 0

    def is_valid(self):
        # Check if the current state is valid
        return (0 <= self.cannibalLeft <= 3 and 0 <= self.missionaryLeft <= 3 and
                0 <= self.cannibalRight <= 3 and 0 <= self.missionaryRight <= 3 and
                (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and
                (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight))

    def __eq__(self, other):
        return (self.cannibalLeft, self.missionaryLeft, self.boat,
                self.cannibalRight, self.missionaryRight) == (other.cannibalLeft, other.missionaryLeft, other.boat,
                                                              other.cannibalRight, other.missionaryRight)

    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat,
                     self.cannibalRight, self.missionaryRight))


def successors(cur_state):
    children = []
    if cur_state.boat == 'left':
        # Generate new states by moving people from left to right
        moves = [
            (0, 2), (2, 0), (1, 1), (0, 1), (1, 0)  # possible moves: (missionaries, cannibals)
        ]
    else:
        # Generate new states by moving people from right to left
        moves = [
            (0, 2), (2, 0), (1, 1), (0, 1), (1, 0)
        ]

    for m, c in moves:
        # Depending on the boat's location, update the state
        if cur_state.boat == 'left':
            new_state = State(cur_state.cannibalLeft - c, cur_state.missionaryLeft - m, 'right',
                              cur_state.cannibalRight + c, cur_state.missionaryRight + m)
        else:
            new_state = State(cur_state.cannibalLeft + c, cur_state.missionaryLeft + m, 'left',
                              cur_state.cannibalRight - c, cur_state.missionaryRight - m)
        
        # Add valid new states
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    
    return children


def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.is_goal():
        return initial_state

    frontier = [initial_state]
    explored = set()

    while frontier:
        state = frontier.pop(0)

        if state.is_goal():
            return state

        explored.add(state)

        for child in successors(state):
            if child not in explored and child not in frontier:
                frontier.append(child)

    return None


def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    
    for state in reversed(path):
        print(f"({state.cannibalLeft}, {state.missionaryLeft}, {state.boat}, {state.cannibalRight}, {state.missionaryRight})")


def main():
    solution = breadth_first_search()
    print("Missionaries and Cannibals solution:")
    print("cannibalLeft missionaryLeft boat cannibalRight missionaryRight")
    print_solution(solution)


if __name__ == "__main__":
    main()
