import sys

tree = {}
count = 0
visited = []

def compute_count(planet, hops):

    global count

    try:
        orbiting_planets = tree[planet]
    except KeyError:
        orbiting_planets = []

    count += len(orbiting_planets)

    for orbiting_planet in orbiting_planets:
        count += hops
        compute_count(orbiting_planet, hops + 1)

def find_orbital_transfers(source, destination, hops):

    visited.append(source)
    planets = tree[source]
    if destination in planets:
        print('Number of orbital transfers = {}'.format(hops - 1))
    else:
        for planet in planets:
            if planet not in visited:
                find_orbital_transfers(planet, destination, hops + 1)

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 day6.py input.txt')
        return

    with open(sys.argv[1]) as f:
        orbits = f.read()
        orbits = orbits.strip().split('\n')

    for orbit in orbits:
        planets = orbit.split(')')

        tree[planets[0]] = []
        tree[planets[1]] = []

    for orbit in orbits:
        planets = orbit.split(')')
        tree[planets[0]].append(planets[1])
        tree[planets[1]].append(planets[0])

    # Remove line 47 and 52 and uncomment the below lines for part 1
    #compute_count('COM', 0)
    #print('Count = {}'.format(count))

    find_orbital_transfers('YOU', 'SAN', 0)

if __name__ == '__main__':
    main()