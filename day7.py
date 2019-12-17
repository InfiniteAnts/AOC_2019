import sys
import itertools

input_signal = 0
opcodes_orig = []
j = 0
amplifiers = {}
amplifier_cursors = [0, 0, 0, 0, 0]
output_to_thrusters = []

def run_program(opcodes, amp_input, permutation, i, first_output_signal):

    global output_signal
    global j
    global opcodes_orig
    global amplifiers
    global amplifier_names
    global amplifier_cursors

    # Instruction pointer
    # i = 0
    while True:

        operation = int(opcodes[i][-2] + opcodes[i][-1])
        parameter_mode_1 = int(opcodes[i][-3])
        parameter_mode_2 = int(opcodes[i][-4])

        # Addition operation
        if operation == 1:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]


            opcodes[int(opcodes[i + 3])] = str(int(parameter_1) + int(parameter_2))
            i += 4

        # Multiplication operation
        elif operation == 2:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]

            opcodes[int(opcodes[i + 3])] = str(int(parameter_1) * int(parameter_2))
            i += 4

        # Read input operation
        elif operation == 3:
            opcodes[int(opcodes[i + 1])] = amp_input.pop(0)
            i += 2

        # Write output operation
        elif operation == 4:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            output_signal = int(parameter_1)

            # Update the cursor so we start from the proper point when switching back to this amplifier
            amplifier_cursors[j] = i + 2

            if j < 4:
                j += 1
            else:
                j = 0

            # Phase setting will be the first input signal to an amplifier
            if first_output_signal[j]:

                amp_input.append(permutation[j])
                first_output_signal[j] = False

            amp_input.append(output_signal)

            run_program(amplifiers[amplifier_names[j]], amp_input, permutation, amplifier_cursors[j], first_output_signal)
            amp_input = []
            return

        # Jump-if-true operation
        elif operation == 5:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]

            if int(parameter_1) != 0:
                i = int(parameter_2)
            else:
                i += 3

        # Jump-if-false operation
        elif operation == 6:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]

            if int(parameter_1) == 0:
                i = int(parameter_2)
            else:
                i += 3

        # Less than operation
        elif operation == 7:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]

            if int(parameter_1) < int(parameter_2):
                opcodes[int(opcodes[i + 3])] = str(1).zfill(5)
            else:
                opcodes[int(opcodes[i + 3])] = str(0).zfill(5)

            i += 4

        # Equals operation
        elif operation == 8:

            parameter_1 = opcodes[i + 1]
            if parameter_mode_1 == 0:
                parameter_1 = opcodes[int(opcodes[i + 1])]

            parameter_2 = opcodes[i + 2]
            if parameter_mode_2 == 0:
                parameter_2 = opcodes[int(opcodes[i + 2])]

            if int(parameter_1) == int(parameter_2):
                opcodes[int(opcodes[i + 3])] = str(1).zfill(5)
            else:
                opcodes[int(opcodes[i + 3])] = str(0).zfill(5)

            i += 4

        # Break operation
        elif operation == 99:
            break

        else:
            print('Unknown opcode = {} @ {}'.format(opcodes[i], i))
            return

    return


def main():

    global input_signal
    global output_signal
    global j
    global amplifiers
    global amplifier_names
    global amplifier_cursors

    if len(sys.argv) != 2:
        print('Usage: python3 day2.py input.txt')
        return

    infile = open(sys.argv[1], 'r')
    data = infile.read()
    opcodes = data.strip().split(',')
    opcodes_orig = [i.zfill(5) for i in opcodes]
    infile.close()

    permutations = itertools.permutations(range(5, 10))

    amplifier_names = 'ABCDE'

    # For each permutation
    for permutation in permutations:

        # Set the output signal flags
        first_output_signal = [False, True, True, True, True]

        # Reset the amplifier cursors back to zero
        amplifier_cursors = [0, 0, 0, 0, 0]

        # Reset the opcodes memory array
        for amplifier in amplifier_names:
            amplifiers[amplifier] = opcodes_orig.copy()

        # Reset the input signal and output signal
        input_signal = 0
        output_signal = 0
        j = 0

        # The first 2 inputs to the amplifier are the phase setting and the input signal
        amp_input = [permutation[j], input_signal]

        # Run the program
        run_program(amplifiers[amplifier_names[j]], amp_input, permutation, amplifier_cursors[j], first_output_signal)

        # Record the output to thrusters
        output_to_thrusters.append(output_signal)

    print('Max output to the thrusters = {}'.format(max(output_to_thrusters)))

if __name__ == '__main__':
    main()

