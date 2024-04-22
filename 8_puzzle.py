import heapq

class PuzzleState:
    def __init__(self, g_value, h_value, empty_row, empty_col, matrix):
        self.g_value = g_value
        self.h_value = h_value
        self.empty_row = empty_row
        self.empty_col = empty_col
        self.matrix = matrix

    def __lt__(self, other):
        return (self.g_value + self.h_value) < (other.g_value + other.h_value)

    def __eq__(self, other):
        return (self.g_value + self.h_value) == (other.g_value + other.h_value)

def is_visited(visited, new_matrix):
    # Check whether new_matrix is already visited or not
    for visited_matrix in visited:
        if visited_matrix == new_matrix:
            return True
    return False

def get_new_matrix(original, i, j, new_i, new_j):
    # Find the resultant matrix after swapping
    new_matrix = [row[:] for row in original]
    new_matrix[i][j], new_matrix[new_i][new_j] = new_matrix[new_i][new_j], new_matrix[i][j]
    return new_matrix

def count_misplaced(original, matrix):
    # Count the number of misplaced cells
    count = 0
    for i in range(len(original)):
        for j in range(len(original[0])):
            if original[i][j] != matrix[i][j]:
                count += 1
    return count

def print_state(state, direction):
    directions = ["up", "right", "down", "left"]
    print("Shifting", directions[direction])
    print("Shuffled matrix:", state.matrix)
    print("h_value:", state.h_value)
    print("g_value:", state.g_value)
    print()

def solve_puzzle(initial, goal):
    rows, cols = len(initial), len(initial[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [initial]
    paths = []
    source = PuzzleState(0, count_misplaced(initial, goal), 0, 0, initial)
    pq = [(0, source)]

    while pq:
        _, curr_state = heapq.heappop(pq)
        paths.append(curr_state)
        if curr_state.matrix == goal:
            print("Goal state reached")
            return curr_state, paths

        for direction in range(4):
            new_row = dx[direction] + curr_state.empty_row
            new_col = dy[direction] + curr_state.empty_col
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_matrix = get_new_matrix(curr_state.matrix, curr_state.empty_row,
                                            curr_state.empty_col, new_row, new_col)
                new_state = PuzzleState(curr_state.g_value + 1, count_misplaced(new_matrix, goal),
                                        new_row, new_col, new_matrix)
                if not is_visited(visited, new_matrix):
                    heapq.heappush(pq, (new_state.g_value + new_state.h_value, new_state))
                    print_state(new_state, direction)
                    visited.append(new_matrix)
    print("Unsolvable puzzle")
    return None, paths

# Example puzzle
initial_state = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]

target, paths = solve_puzzle(initial_state, goal_state)
print("h_value:", target.h_value)
print("g_value:", target.g_value)
print("\nPath of Matrices:\n")
for state in paths:
    for row in state.matrix:
        print(*row)
    print()

