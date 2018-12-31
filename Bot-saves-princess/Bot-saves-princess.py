#

def displayPathtoPrincess(n,grid):
    # Finding the princess & bot location
    break_outer_loop = False
    bot_index = (-1,-1)
    princess_index = (-1, -1)
    for row in range(n):
        for column in range(n):
            if grid[row][column] == 'p':
                princess_index = (row,column)
                break_outer_loop = True if bot_index[0] != -1 else False
                break
            if grid[row][column] == 'm':
                bot_index = (row,column)
                break_outer_loop = True if princess_index[0] != -1 else False
                break

        if break_outer_loop:
            break

    if princess_index[1] == c:
        # both bot and princess in the same column
        move = "UP" if princess_index[0] < bot_index[0] else "DOWN"
    else:
        # move until both bot and princess comes to same column
        move = "LEFT" if princess_index[1] < bot_index[1]  else "RIGHT"
    return move



n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))