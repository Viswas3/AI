class Graph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.adjacency_matrix = [[0 for _ in range(vertices_count)] for _ in range(vertices_count)]

    # Function to check if the current color assignment is safe for vertex v
    def is_safe(self, vertex, color_assignment, color):
        for i in range(self.vertices_count):
            # Check if there's an adjacent vertex with the same color
            if self.adjacency_matrix[vertex][i] == 1 and color_assignment[i] == color:
                return False
        return True

    # Recursive function to solve the graph coloring problem
    def graph_coloring_util(self, num_colors, color_assignment, vertex):
        # Base case: if all vertices are colored
        if vertex == self.vertices_count:
            return True

        # Try different colors for the current vertex
        for color in range(1, num_colors + 1):
            # Check if assigning the current color to the vertex is safe
            if self.is_safe(vertex, color_assignment, color):
                color_assignment[vertex] = color
                # Recur for the next vertex
                if self.graph_coloring_util(num_colors, color_assignment, vertex + 1):
                    return True
                # Backtrack if coloring with the current color doesn't lead to a solution
                color_assignment[vertex] = 0

    # Main function to solve the graph coloring problem
    def graph_coloring(self, num_colors):
        color_assignment = [0] * self.vertices_count
        # Try to color the graph starting from vertex 0
        if not self.graph_coloring_util(num_colors, color_assignment, 0):
            print("Solution does not exist")
            return False

        print("Solution exists and following are the assigned colors:")
        for color in color_assignment:
            print(color, end=" ")

        return True

# Example usage:
graph = Graph(4)
graph.adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

num_colors = 3  # Number of colors
graph.graph_coloring(num_colors)

