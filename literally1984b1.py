from fractions import Fraction
import heapq

def solve(N: int) -> tuple[int, int]:
    """
    Return a tuple containing the coordinates X and Y for the given address N.
    """
    def findHouseCoord(N):
        # Generate possible coordinates and filter based on visibility
        slopes = set()

        # priority queue
        pq = []
        limit = 200000

        for x in range(1, limit + 1):
            for y in range(1, limit + 1):
                slope = Fraction(y, x)

                # If this slope hasn't been encountered before, it's visible (another house/coord isnt blocking it)
                if slope not in slopes:
                    distance = x+y
                    heapq.heappush(pq, (distance,x,y)) # manhattan distance, x, y
                    slopes.add(slope)

        # Define sorting key functions
        for _ in range(N):
            _, x, y = heapq.heappop(pq)

        return (x,y)
    
    # Get the coordinates for address N
    return findHouseCoord(N)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        # Print the coordinates for each test case
        print(*solve(N))

if __name__ == "__main__":
    main()
