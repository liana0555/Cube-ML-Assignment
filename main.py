from dfs import dfs_search           # Searching in depth
from bfs import bfs_search           # Search width
from astar import astar_search       # Search with an asterisk
from cube import Cube                # Model
from utils import measure_time       # Function for time measurement

if __name__ == "__main__":
    cube = Cube() # Create an assembled cube
    
    # Disassembling the cube
    scrambled = cube.scramble(steps=4)
    scrambled.print_cube()


    choice = input("\nPick an algorithm (dfs / bfs / astar): ").strip().lower()
    
    if choice == "dfs":
        result, time_taken = measure_time(dfs_search, scrambled, 7)

    elif choice == "bfs":
        result, time_taken = measure_time(bfs_search, scrambled, 7)

    elif choice == "astar":
        result, time_taken = measure_time(astar_search, scrambled)
    else:
        print("Wrong")
        exit()

    # Solution output
    if result:
        print("\nDecision:")
        for step in result:
            step.print_cube()  
            print()
        print(f"Time: {time_taken:.6f} seconds")

        #Testing
        if result[-1].is_solved():
            print("\n The cube has been successfully assembled.")
        else:
            print("\n Error")
    else:
        print("Solution not found.")
