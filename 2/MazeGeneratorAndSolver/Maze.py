import random
from collections import deque

class MazeGenerator:
    """Generate random solvable mazes using DFS algorithm"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Make sure dimensions are odd for proper maze structure
        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1
        self.width = width
        self.height = height
        
        # Initialize maze with all walls (1 = wall, 0 = path)
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        
    def generate_maze(self, start_x=1, start_y=1):
        """Generate maze using Depth-First Search (DFS) with backtracking"""
        # Stack for DFS
        stack = [(start_x, start_y)]
        
        # Mark starting position as path
        self.maze[start_y][start_x] = 0
        
        # Directions: right, down, left, up
        directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        
        while stack:
            current_x, current_y = stack[-1]
            
            # Get all valid neighbors
            neighbors = []
            for dx, dy in directions:
                new_x, new_y = current_x + dx, current_y + dy
                
                # Check if neighbor is within bounds and is a wall
                if (0 < new_x < self.width - 1 and 
                    0 < new_y < self.height - 1 and 
                    self.maze[new_y][new_x] == 1):
                    neighbors.append((new_x, new_y))
            
            if neighbors:
                # Choose random neighbor
                next_x, next_y = random.choice(neighbors)
                
                # Remove wall between current cell and chosen neighbor
                wall_x = current_x + (next_x - current_x) // 2
                wall_y = current_y + (next_y - current_y) // 2
                
                self.maze[wall_y][wall_x] = 0
                self.maze[next_y][next_x] = 0
                
                # Add neighbor to stack
                stack.append((next_x, next_y))
            else:
                # Backtrack
                stack.pop()
        
        # Ensure start and end points are open
        self.maze[1][1] = 0  # Start
        self.maze[self.height - 2][self.width - 2] = 0  # End
        
        return self.maze
    
    def print_maze(self, path=None, solution_path=None):
        """Print maze with optional path highlighting"""
        symbols = {
            1: '█',  # Wall
            0: ' ',  # Path
            'S': 'S',  # Start
            'E': 'E',  # End
            '.': '.',  # Visited during search
            '*': '*'   # Solution path
        }
        
        # Create display maze
        display = [[self.maze[y][x] for x in range(self.width)] for y in range(self.height)]
        
        # Mark start and end
        display[1][1] = 'S'
        display[self.height - 2][self.width - 2] = 'E'
        
        # Mark search path if provided
        if path:
            for x, y in path:
                if display[y][x] == 0:
                    display[y][x] = '.'
        
        # Mark solution path if provided
        if solution_path:
            for x, y in solution_path:
                if display[y][x] not in ['S', 'E']:
                    display[y][x] = '*'
        
        # Print maze
        for row in display:
            print(''.join(symbols.get(cell, str(cell)) for cell in row))
        print()


class MazeSolver:
    """Solve mazes using DFS and BFS algorithms"""
    
    def __init__(self, maze):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.start = (1, 1)
        self.end = (self.width - 2, self.height - 2)
    
    def get_neighbors(self, x, y):
        """Get valid neighboring cells"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down, right, up, left
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check bounds and if cell is a path
            if (0 <= new_x < self.width and 
                0 <= new_y < self.height and 
                self.maze[new_y][new_x] == 0):
                neighbors.append((new_x, new_y))
        
        return neighbors
    
    def solve_dfs(self):
        """Solve maze using Depth-First Search"""
        stack = [self.start]
        visited = set()
        parent = {}
        path_taken = []
        
        visited.add(self.start)
        parent[self.start] = None
        
        while stack:
            current = stack.pop()
            path_taken.append(current)
            
            if current == self.end:
                # Reconstruct path
                solution_path = []
                while current is not None:
                    solution_path.append(current)
                    current = parent[current]
                solution_path.reverse()
                
                return solution_path, path_taken
            
            # Explore neighbors
            neighbors = self.get_neighbors(current[0], current[1])
            # Randomize for more interesting paths
            random.shuffle(neighbors)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)
        
        return None, path_taken  # No solution found
    
    def solve_bfs(self):
        """Solve maze using Breadth-First Search"""
        queue = deque([self.start])
        visited = set()
        parent = {}
        path_taken = []
        
        visited.add(self.start)
        parent[self.start] = None
        
        while queue:
            current = queue.popleft()
            path_taken.append(current)
            
            if current == self.end:
                # Reconstruct path
                solution_path = []
                while current is not None:
                    solution_path.append(current)
                    current = parent[current]
                solution_path.reverse()
                
                return solution_path, path_taken
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current[0], current[1]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        return None, path_taken  # No solution found


def demonstrate_maze_system():
    """Demonstrate maze generation and solving"""
    print("🧩 MAZE GENERATOR AND SOLVER DEMO 🧩")
    print("=" * 50)
    
    # Generate a maze
    print("1. GENERATING MAZE...")
    generator = MazeGenerator(21, 21)  # Odd dimensions for proper maze
    maze = generator.generate_maze()
    
    print("Generated Maze:")
    print("S = Start, E = End, █ = Wall, (space) = Path")
    generator.print_maze()
    
    # Create solver
    solver = MazeSolver(maze)
    
    # Solve with DFS
    print("2. SOLVING WITH DFS (DEPTH-FIRST SEARCH)...")
    dfs_solution, dfs_path = solver.solve_dfs()
    
    if dfs_solution:
        print(f"DFS found solution in {len(dfs_solution)} steps!")
        print(f"DFS explored {len(dfs_path)} cells")
        print("DFS Solution (* = solution path, . = explored):")
        generator.print_maze(path=dfs_path, solution_path=dfs_solution)
    else:
        print("DFS couldn't find a solution!")
    
    # Solve with BFS
    print("3. SOLVING WITH BFS (BREADTH-FIRST SEARCH)...")
    bfs_solution, bfs_path = solver.solve_bfs()
    
    if bfs_solution:
        print(f"BFS found solution in {len(bfs_solution)} steps!")
        print(f"BFS explored {len(bfs_path)} cells")
        print("BFS Solution (* = solution path, . = explored):")
        generator.print_maze(path=bfs_path, solution_path=bfs_solution)
    else:
        print("BFS couldn't find a solution!")
    
    # Compare algorithms
    if dfs_solution and bfs_solution:
        print("4. ALGORITHM COMPARISON:")
        print(f"DFS solution length: {len(dfs_solution)} steps")
        print(f"BFS solution length: {len(bfs_solution)} steps")
        print(f"DFS cells explored: {len(dfs_path)}")
        print(f"BFS cells explored: {len(bfs_path)}")
        print(f"BFS finds optimal path: {len(bfs_solution) <= len(dfs_solution)}")


def interactive_maze():
    """Interactive maze generator and solver"""
    print("\n🎮 INTERACTIVE MAZE SYSTEM 🎮")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Generate small maze (11x11)")
        print("2. Generate medium maze (21x21)")
        print("3. Generate large maze (31x31)")
        print("4. Custom size maze")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            size = 11
        elif choice == "2":
            size = 21
        elif choice == "3":
            size = 31
        elif choice == "4":
            try:
                size = int(input("Enter maze size (odd number, 5-51): "))
                if size < 5 or size > 51:
                    print("Size must be between 5 and 51!")
                    continue
                if size % 2 == 0:
                    size += 1
                    print(f"Adjusted to odd size: {size}")
            except ValueError:
                print("Please enter a valid number!")
                continue
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")
            continue
        
        # Generate maze
        print(f"\nGenerating {size}x{size} maze...")
        generator = MazeGenerator(size, size)
        maze = generator.generate_maze()
        
        print("Generated Maze:")
        generator.print_maze()
        
        # Choose solving method
        solver = MazeSolver(maze)
        
        solve_choice = input("Solve with (1) DFS, (2) BFS, or (3) Both? ").strip()
        
        if solve_choice in ["1", "3"]:
            print("Solving with DFS...")
            dfs_solution, dfs_path = solver.solve_dfs()
            if dfs_solution:
                print(f"DFS Solution ({len(dfs_solution)} steps):")
                generator.print_maze(solution_path=dfs_solution)
            else:
                print("No solution found with DFS!")
        
        if solve_choice in ["2", "3"]:
            print("Solving with BFS...")
            bfs_solution, bfs_path = solver.solve_bfs()
            if bfs_solution:
                print(f"BFS Solution ({len(bfs_solution)} steps):")
                generator.print_maze(solution_path=bfs_solution)
            else:
                print("No solution found with BFS!")


def test_algorithms():
    """Test maze generation and solving algorithms"""
    print("🧪 ALGORITHM TESTING 🧪")
    print("=" * 30)
    
    sizes = [9, 15, 21]
    
    for size in sizes:
        print(f"\nTesting {size}x{size} maze:")
        
        # Generate maze
        generator = MazeGenerator(size, size)
        maze = generator.generate_maze()
        solver = MazeSolver(maze)
        
        # Test both algorithms
        dfs_solution, dfs_path = solver.solve_dfs()
        bfs_solution, bfs_path = solver.solve_bfs()
        
        print(f"DFS: {'✓' if dfs_solution else '✗'} "
              f"({len(dfs_solution) if dfs_solution else 0} steps, "
              f"{len(dfs_path)} explored)")
        
        print(f"BFS: {'✓' if bfs_solution else '✗'} "
              f"({len(bfs_solution) if bfs_solution else 0} steps, "
              f"{len(bfs_path)} explored)")
        
        if dfs_solution and bfs_solution:
            print(f"BFS optimal: {'✓' if len(bfs_solution) <= len(dfs_solution) else '✗'}")


def main():
    """Main program"""
    print("🏁 Welcome to Maze Generator and Solver! 🏁")
    print("This program demonstrates:")
    print("- Maze generation using DFS with backtracking")
    print("- Maze solving using DFS and BFS algorithms")
    print("- Text-based visualization")
    print("- Algorithm comparison")
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Run complete demonstration")
        print("2. Interactive maze generator")
        print("3. Test algorithms")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            demonstrate_maze_system()
        elif choice == "2":
            interactive_maze()
        elif choice == "3":
            test_algorithms()
        elif choice == "4":
            print("Thanks for using the Maze System! 🎉")
            break
        else:
            print("Please enter 1, 2, 3, or 4")


if __name__ == "__main__":
    main()