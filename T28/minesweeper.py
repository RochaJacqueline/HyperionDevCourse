# Task 1

grid = [
        ["#", "-", "-", "-"],
        ["-", "#", "-", "#"],
        ["#", "#", "-", "#"],
        ["-", "#", "#", "-"],
    ]

def count_mines(i, j, grid):
    """Function that takes a row, column and grid, and counts the number of mines for each position"""
    count = 0

    # Checking NW position
    if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j -1] == "#":
        count += 1
    # Checking N position
    if i - 1 >= 0 and grid[i - 1][j] == "#":
        count += 1
    # Checking NE position
    if i - 1 >= 0 and j + 1 < len(grid[i]) and grid[i - 1][j + 1] == "#":
        count += 1
    # Checking W position
    if j - 1 >= 0 and grid[i][j -1] == "#":
        count += 1
    # Checking E position
    if j + 1 < len(grid[i]) and grid[i][j + 1] == "#":
        count += 1
    # Checking SW position
    if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == "#":
        count += 1
    # Checking S position
    if i + 1 < len(grid) and grid[i + 1][j] == "#":
        count += 1
    # Checking SE position
    if i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] == "#":
        count += 1

    return count

def minesweeper(grid):
    """Function that takes a minesweeper grid, and returns a grid showing the mines count"""

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == "-":
                grid[i][j] = str(count_mines(i, j, grid))

        print(grid[i])

minesweeper(grid)