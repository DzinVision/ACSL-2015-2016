# Vid Drobnič
# Gimnazija Vič, 3.b
# Intermediate 3
# Language: Python 3.5.1


# Debugging
def print_grid(grid):
    for y in range(6):
        for x in range(6):
            print(grid[y * 6 + x] + ' ', end='')
        print('')


def solve(data):
    grid = ['.' for _ in range(36)]

    for i in range(4):
        index = int(data[i]) - 1
        grid[index] = 'X'

    for i in range(5, len(data) - 1, 2):
        letter = data[i]
        index = int(data[i + 1]) - 1

        move = 0
        if index % 6 == 0:
            move = 1
        elif index % 6 == 5:
            move = -1
        elif index // 6 == 0:
            move = 6
        elif index // 6 == 5:
            move = -6

        while True:
            index += move
            if grid[index] != 'X':
                grid[index] = letter
                break

    while True:
        solved = True
        for y in range(1, 5):
            for x in range(1, 5):
                if grid[y * 6 + x] == '.':
                    solved = False
                    row = {'A', 'B', 'C'}
                    column = {'A', 'B', 'C'}
                    for x1 in range(1, 5):
                        value = grid[y * 6 + x1]
                        if value in row:
                            row.remove(value)

                    for y1 in range(1, 5):
                        value = grid[y1 * 6 + x]
                        if value in column:
                            column.remove(value)

                    result = row & column
                    if len(result) == 1:
                        grid[y * 6 + x] = result.pop()

        if solved:
            break

    # print_grid(grid)
    print(grid[int(data[len(data) - 1]) - 1])

for _ in range(5):
    solve(input().split())
