import random

def printGrid(grid):
    for i in grid:
        for j in i:
            print(j,end = "\t")
        print()

def getCount(grid,i,j):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    if i>0 and grid[i-1][j]=='*':
        count += 1
    if i<rows-1 and grid[i+1][j]=='*':
        count += 1
    if j>0 and grid[i][j-1]=='*':
        count += 1
    if j<cols-1 and grid[i][j+1]=='*':
        count += 1
    if i>0 and j>0 and grid[i-1][j-1]=='*':
        count += 1
    if i>0 and j<cols-1 and grid[i-1][j+1]=='*':
        count += 1
    if i<rows-1 and j>0 and grid[i+1][j-1]=='*':
        count += 1
    if i<rows-1 and j<cols-1 and grid[i+1][j+1]=='*':
        count += 1
    return count

def generateGrid(rows,cols,n):
    grid = [[' ' for i in range(rows)] for j in range(cols)]
    for k in range(n):
        i = random.randint(0,rows-1)
        j = random.randint(0,cols-1)
        while grid[i][j]=='*':
            i = random.randint(0,rows-1)
            j = random.randint(0,cols-1)
        grid[i][j] = "*"


    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ' ':
                x = str(getCount(grid,i,j))
                if x=='0':
                    grid[i][j] = ' '
                else:
                    grid[i][j] = x
    
    # printGrid(grid)
    return grid


generateGrid(10,10,50)
    