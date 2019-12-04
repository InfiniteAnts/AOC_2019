import sys
import numpy as np

def plot_wire(grid, wire, cursor_x, cursor_y, z):

    steps = 1

    for path in wire:

        # Go Right
        if path[0] == 'R':

            for i in range(1, int(path[1:]) + 1):
                if grid[cursor_x + i][cursor_y][z] == 0:
                    grid[cursor_x + i][cursor_y][z] = steps
                steps += 1
            cursor_x += int(path[1:])

        # Go Left
        elif path[0] == 'L':

            for i in range(1, int(path[1:]) + 1):
                if grid[cursor_x - i][cursor_y][z] == 0:
                    grid[cursor_x - i][cursor_y][z] = steps
                steps += 1
            cursor_x -= int(path[1:])

        # Go Up
        elif path[0] == 'U':

            for i in range(1, int(path[1:]) + 1):
                if grid[cursor_x][cursor_y + i][z] == 0:
                    grid[cursor_x][cursor_y + i][z] = steps
                steps += 1
            cursor_y += int(path[1:])

        # Go Down
        elif path[0] == 'D':

            for i in range(1, int(path[1:]) + 1):
                if grid[cursor_x][cursor_y - i][z] == 0:
                    grid[cursor_x][cursor_y - i][z] = steps
                steps += 1
            cursor_y -= int(path[1:])

def get_intersections(grid, central_port_x, central_port_y):

    intersections = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][0] > 0 and grid[i][j][1] > 0 and not (i == central_port_x and j == central_port_y):
                intersections.append(grid[i][j])

    return intersections

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py input.txt')
        return

    wire = {}
    i = 0

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

        for line in lines:
            wire[i] = line.split(',')
            i += 1

    central_port_x = 7000
    central_port_y = 7000
    grid = np.zeros((central_port_x * 2, central_port_y * 2, len(wire)), dtype=np.int32)
    z = 0

    # Plot each of the wires on the grid
    print('Plotting wires.....')
    for each_wire in wire:
        plot_wire(grid, wire[each_wire], central_port_x, central_port_y, z)
        z += 1

    # Get intersections
    print('Getting intersections.....')
    intersections = get_intersections(grid, central_port_x, central_port_y)

    # Calculate number of steps for each intersection
    print('Calculating number of steps....')
    no_of_steps = []
    for intersection in intersections:
        steps = intersection[0] + intersection[1]
        no_of_steps.append(steps)

    min_no_of_steps = min(no_of_steps)
    print('Minimum number of steps = {}'.format(min_no_of_steps))

    # for row in grid:
    #     for cell in row:
    #         print(cell, end='')
    #     print('')

if __name__ == '__main__':
    main()