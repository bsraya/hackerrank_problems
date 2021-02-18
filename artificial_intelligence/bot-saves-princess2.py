def nextMove(n, r, c, grid):
    for index, row in enumerate(grid):
        if 'p' in row:  # locate the princess
            princess = (index, row.index('p'))
        if 'm' in row:  # locate the bot
            bot = (index, row.index('m'))

    delta_row = princess[0] - bot[0]
    delta_col = princess[1] - bot[1]

    if not delta_row == 0:
        if(delta_row) < 0:
            next_move = 'UP'
        else:
            next_move = 'DOWN'
    if not delta_col == 0:
        if(delta_col) < 0:
            next_move = 'LEFT'
        else:
            next_move = 'RIGHT'
    return next_move


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
