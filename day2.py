import sys
import itertools

def run_program(opcodes, i, j):
    opcodes[1] = i
    opcodes[2] = j

    i = 0

    while True:

        if opcodes[i] == 1:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] + opcodes[opcodes[i + 2]]
            i += 4

        elif opcodes[i] == 2:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] * opcodes[opcodes[i + 2]]
            i += 4

        elif opcodes[i] == 99:
            break

    return opcodes[0]

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 day2.py input.txt')
        return

    infile = open(sys.argv[1], 'r')
    data = infile.read()
    opcodes_orig = data.strip().split(',')
    opcodes = [int(i) for i in opcodes_orig]
    infile.close()

    iterable = itertools.product(range(0, 100), range(0, 100))

    for iteration in iterable:
        if run_program(opcodes, iteration[0], iteration[1]) == 19690720:
            noun = opcodes[1]
            verb = opcodes[2]
            output = 100 * noun + verb
            print(output)
            break

        opcodes = [int(i) for i in opcodes_orig]

if __name__ == '__main__':
    main()