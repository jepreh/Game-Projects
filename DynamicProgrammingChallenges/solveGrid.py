# This dynamic programming function solves the total number of paths to be taken in a x by y grid.
# The function starts from the top left of the grid to the bottom right, while only moving right or down by 1 each step.
# Each solved path is saved to the memo dict, where key = x, y and value = the number of paths for the grid size.
# Since the grid is symmetrical, x or y sizes of the grid have the same number of solved paths, if (REVERSE_KEY in memo): return memo[REVERSE_KEY] avoids further duplicated calculations

def solveGrid(x, y, memo = {}):
    KEY = (x, y)
    REVERSE_KEY = (y, x)
    if (KEY in memo):
        return memo[KEY]
    if (REVERSE_KEY in memo):
        return memo[REVERSE_KEY]
    if x == 0 or y == 0:
        return 0
    if x == 1 and y == 1:
        return 1
    
    memo[KEY] = solveGrid(x - 1, y, memo) + solveGrid(x, y - 1, memo)
    return memo[KEY]

def main():
    print(solveGrid(3, 10))
    print(solveGrid(5, 10))
    print(solveGrid(2, 3))
    print(solveGrid(2, 7))
    print(solveGrid(3, 2))

if __name__ == "__main__":
    main()
    exit()