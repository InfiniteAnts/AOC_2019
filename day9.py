import sys
import itertools


def run_program(opcodes):

    # Instruction pointer
    i = 0

    # Relative base
    relative_base = 0

    while True:

        operation = int(opcodes[i][-2] + opcodes[i][-1])
        parameter_mode_1 = int(opcodes[i][-3])
        parameter_mode_2 = int(opcodes[i][-4])

        # Addition operation
        if operation == 1:

            parameter_mode_3 = int(opcodes[i][-5])

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if parameter_mode_3 == 0:
                opcodes[int(opcodes[i + 3])] = str(int(parameter_1) + int(parameter_2))
            elif parameter_mode_3 == 2:
                opcodes[relative_base + int(opcodes[i + 3])] = str(int(parameter_1) + int(parameter_2))

            i += 4

        # Multiplication operation
        elif operation == 2:

            parameter_mode_3 = int(opcodes[i][-5])

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if parameter_mode_3 == 0:
                opcodes[int(opcodes[i + 3])] = str(int(parameter_1) * int(parameter_2))
            elif parameter_mode_3 == 2:
                opcodes[relative_base + int(opcodes[i + 3])] = str(int(parameter_1) * int(parameter_2))

            i += 4

        # Read input operation
        elif operation == 3:

            if parameter_mode_1 == 0:
                opcodes[int(opcodes[i + 1])] = input('Please enter system ID: ')
            elif parameter_mode_1 == 2:
                opcodes[relative_base + int(opcodes[i + 1])] = input('Please enter system ID: ')

            i += 2

        # Write input operation
        elif operation == 4:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            print(int(parameter_1))
            i += 2

        # Jump-if-true operation
        elif operation == 5:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if int(parameter_1) != 0:
                i = int(parameter_2)
            else:
                i += 3

        # Jump-if-false operation
        elif operation == 6:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if int(parameter_1) == 0:
                i = int(parameter_2)
            else:
                i += 3

        # Less than operation
        elif operation == 7:

            parameter_mode_3 = int(opcodes[i][-5])

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if int(parameter_1) < int(parameter_2):
                if parameter_mode_3 == 0:
                    opcodes[int(opcodes[i + 3])] = str(1).zfill(5)
                elif parameter_mode_3 == 2:
                    opcodes[relative_base + int(opcodes[i + 3])] = str(1).zfill(5)
            else:
                if parameter_mode_3 == 0:
                    opcodes[int(opcodes[i + 3])] = str(0).zfill(5)
                elif parameter_mode_3 == 2:
                    opcodes[relative_base + int(opcodes[i + 3])] = str(0).zfill(5)

            i += 4

        # Equals operation
        elif operation == 8:

            parameter_mode_3 = int(opcodes[i][-5])

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]
            elif parameter_mode_2 == 2:
                parameter_2 = opcodes[relative_base + int(opcodes[i + 2])]

            if int(parameter_1) == int(parameter_2):
                if parameter_mode_3 == 0:
                    opcodes[int(opcodes[i + 3])] = str(1).zfill(5)
                elif parameter_mode_3 == 2:
                    opcodes[relative_base + int(opcodes[i + 3])] = str(1).zfill(5)
            else:
                if parameter_mode_3 == 0:
                    opcodes[int(opcodes[i + 3])] = str(0).zfill(5)
                elif parameter_mode_3 == 2:
                    opcodes[relative_base + int(opcodes[i + 3])] = str(0).zfill(5)

            i += 4

        # Relative base offset operation
        elif operation == 9:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]
            elif parameter_mode_1 == 2:
                parameter_1 = opcodes[relative_base + int(opcodes[i + 1])]

            relative_base += int(parameter_1)

            i += 2

        # Break operation
        elif operation == 99:
            break

        else:
            print('Unknown opcode = {} @ {}'.format(opcodes[i], i))
            return

    return


def main():

    if len(sys.argv) != 2:
        print('Usage: python3 day9.py input.txt')
        return

    infile = open(sys.argv[1], 'r')
    data = infile.read()
    opcodes = data.strip().split(',')
    opcodes = [i.zfill(5) for i in opcodes]
    infile.close()

    filler_list = [0] * 3000

    opcodes = opcodes + filler_list

    run_program(opcodes)

if __name__ == '__main__':
    main()

