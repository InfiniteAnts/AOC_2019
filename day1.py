import sys

def compute_fuel(mass, total):

    fuel = (mass // 3) - 2
    if fuel > 0:
        total += fuel
        return compute_fuel(fuel, total)
    else:
        return total

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 day1.py input.txt')
        return

    total_fuel = 0

    with open(sys.argv[1]) as f:
        masses = f.readlines()

        for mass in masses:
            total_fuel += compute_fuel(int(mass), 0)

    print(total_fuel)

if __name__ == '__main__':
    main()