import random

def generateGrid(rows,cols,n):
    grid = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(n):
        i = random.randint(0,rows-1)
        j = random.randint(0,cols-1)
        grid[i][j] = "*"
    for i in grid:
        for j in i:
            print(j,end = " ")
        print()
generateGrid(5,5,9)