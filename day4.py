import sys
import itertools

def main():

    if len(sys.argv) != 3:
        print('Usage: python3 day4.py number1 number2')
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    count = 0

    for i in range(start, end + 1):

        number = str(i)

        never_decrease = True
        not_group = False

        for j in range(len(number) - 1):

            if number[j] > number[j + 1]:
                never_decrease = False
                break

        groups = [list(g) for k, g in itertools.groupby(number)]

        for group in groups:

            if len(group) == 2:
                not_group = True

        if never_decrease and not_group:
            count += 1

    print('Total count = {}'.format(count))

if __name__ == '__main__':
    main()