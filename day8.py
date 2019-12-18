import sys
import numpy as np
from termcolor import colored

def main():

    if len(sys.argv) != 2:
        print('Usage; python3 day8.py input.txt')
        return

    with open(sys.argv[1]) as f:
        data = f.read().strip()

    no_of_layers = int(len(data) / (25 * 6))

    # Creating a final image array
    final_image = np.zeros((25 * 6), dtype=np.int16)

    # Creating a matrix of bools whether pixel is set or not
    set_matrix = np.zeros((25 * 6), dtype=np.int16)

    for i in range(0, no_of_layers):

        for j in range(25 * 6 * i, (25 * 6 * i) + 25 * 6):

            if (set_matrix[(j - (i * 25 * 6))] == 0) and (data[j] == '0'):
                final_image[(j - (i * 25 * 6))] = 0
                set_matrix[(j - (i * 25 * 6))] = 1

            elif (set_matrix[(j - (i * 25 * 6))] == 0) and (data[j] == '1'):
                final_image[(j - (i * 25 * 6))] = 1
                set_matrix[(j - (i * 25 * 6))] = 1

    final_image = final_image.reshape(6, 25)

    print(final_image)

if __name__ == '__main__':
    main()