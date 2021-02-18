#!/usr/local/bin/python3

def displayPathToPrincess(n, grid):
    path = []
    for index, row in enumerate(grid):
        if 'p' in row:  # locate the princess
            princess = (index, row.index('p'))
        if 'm' in row:  # locate the bot
            bot = (index, row.index('m'))
    delta_row = princess[0] - bot[0]
    delta_col = princess[1] - bot[1]

    if(delta_row) < 0:
        row_direction = 'UP'
    else:
        row_direction = 'DOWN'
    if(delta_col) < 0:
        col_direction = 'LEFT'
    else:
        col_direction = 'RIGHT'

    for i in range(abs(delta_row)):
        path.append(row_direction)

    for i in range(abs(delta_col)):
        path.append(col_direction)

    print('\n'.join(path))


m = int(input())
grid = []

for i in range(0, m):
    grid.append(input().strip())
displayPathToPrincess(m, grid)
