
def parseinput(fname):

    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    matrix = [[_ for _ in line.strip()] for line in lines]
    ants = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c = matrix[i][j]
            if c.isalnum():
                if c not in ants.keys():
                    ants[c] = [(i, j)]
                else:
                    ants[c].append((i, j))

    return matrix, ants


def valid_coord(coords, matrix):
    x, y = coords
    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    if x < 0 or x > row:
        return False
    
    if y < 0 or y > col:
        return False

    return True


def calc_anti(ant1, ant2):
    anti1 = ((2*ant1[0] - ant2[0], 2*ant1[1] - ant2[1]))
    anti2 = ((2*ant2[0] - ant1[0], 2*ant2[1] - ant1[1]))
    return anti1, anti2

def calc_anti_2(ant1, ant2, m):

    antis = []

    a1 = ant1
    a2 = ant2
    # backwards
    while True:
        x = 2*a1[0] - a2[0] 
        y = 2*a1[1] - a2[1]

        if valid_coord((x, y), m):
            antis.append((x, y))
            a2 = a1
            a1 = (x, y)
        else:
            break

    a1 = ant1
    a2 = ant2
    # backwards
    while True:
        x = 2*a2[0] - a1[0] 
        y = 2*a2[1] - a1[1]

        if valid_coord((x, y), m):
            antis.append((x, y))
            a1 = a2
            a2 = (x, y)
        else:
            break

    return antis


def part1(fname):
    m, antenna = parseinput(fname)
    anti_nodes = []

    for ant in antenna.keys():
        a = antenna[ant]

        # Get combinations to get anti nodes
        for i in range(len(a) - 1):
            for j in range(i+1, len(a)):
                # Get anti nodes
                anti1, anti2 = calc_anti(a[i], a[j])
                
                # Validate them
                if valid_coord(anti1, m):
                    anti_nodes.append(anti1)

                if valid_coord(anti2, m):
                    anti_nodes.append(anti2)

    # Want unique so return set of anti nodes
    return len(set(anti_nodes))


def part2(fname):
    m, antenna = parseinput(fname)
    anti_nodes = []

    for ant in antenna.keys():
        a = antenna[ant]

        # Get combinations to get anti nodes
        for i in range(len(a) - 1):
            for j in range(i+1, len(a)):
                new_antis = calc_anti_2(a[i], a[j], m)
                anti_nodes += new_antis

    print(anti_nodes)

    # Want unique so return set of anti nodes
    return len(set(anti_nodes))

if __name__ == "__main__":
    
    print("AOC 2024 DAY 8")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("test.txt")
    print(f"Part 2: {out2}")