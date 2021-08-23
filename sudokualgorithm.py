def possible(x,y,n,grid):
    #check row
    for i in range(9):
        if grid[x][i]==n:
            return False
    #check column
    for i in range(9):
        if grid[i][y]==n:
            return False
    #check 3X3 grid
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j]==n:
                return False
    return True

def solve(grid):
    for x in range(9):
        for y in range(9):
            #print(x,y)
            if grid[x][y]==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[x][y]=n
                        if solve():
                            return True
                        grid[x][y]=0
                return False
    return True