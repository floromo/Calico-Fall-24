from collections import deque

def solve(N: int, M: int, G: list[list[int]]) -> int:
    """
    Returns the maximum number of islands for each height threshold `h`.

    N: number of rows in the grid
    M: number of columns in the grid
    G: grid representing the heights of each cell
    """
    # Helper function to perform BFS (Breadth-First Search) to find an island
    def bfs(grid, visited, startRow, startCol, h):
        """
        Perform BFS from the starting cell (startRow, startCol) and mark all 
        connected cells that have a height >= h as visited.

        grid: the grid of land heights
        visited: matrix to keep track of visited cells
        startRow, startCol: starting point for BFS
        h: height threshold
        """
        queue = deque([(startRow, startCol)])  # Initialize the BFS queue with the starting cell
        visited[startRow][startCol] = True  # Mark the starting cell as visited

        # Explore the neighbors using BFS
        while queue:
            row, col = queue.popleft()  # Dequeue the first cell
            # Check all 4 orthogonal directions (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow, newCol = row + dr, col + dc  # New position to explore
                
                # Check if the new position is within bounds and not visited
                if 0 <= newRow < N and 0 <= newCol < M and not visited[newRow][newCol]:
                    # If the height of the neighboring cell is greater than or equal to the threshold
                    if grid[newRow][newCol] >= h:
                        visited[newRow][newCol] = True  # Mark it as visited
                        queue.append((newRow, newCol))  # Add to the queue for further exploration

    # Edge case: If grid is 1x1, there's always one island
    if N == 1 and M == 1:
        return 1

    # Step 1: Find all unique heights in the grid and sort them
    uniqueHeights = sorted(set(height for row in G for height in row))

    maxIslands = 0  # To keep track of the maximum number of islands

    # Step 2: Try each unique height threshold and count islands for each
    for h in uniqueHeights:
        visited = [[False] * M for _ in range(N)]  # Matrix to track visited cells
        islands = 0  # To count islands for the current threshold

        # Step 3: Traverse the entire grid and apply BFS to find all islands
        for i in range(N):
            for j in range(M):
                # If the current cell is above or equal to the height threshold and not visited
                if G[i][j] >= h and not visited[i][j]:
                    bfs(G, visited, i, j, h)  # Perform BFS from this unvisited land cell
                    islands += 1  # Increment the island count for this threshold
        
        # Step 4: Update the maximum number of islands found
        maxIslands = max(maxIslands, islands)

    # Step 5: Return the maximum number of islands found across all height thresholds
    return maxIslands

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [list(map(int, input().split())) for _ in range(N)]
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
