
def part1(fname):
    
    f = open(fname, "r")
    reports = []

    for line in f.readlines():

        l = [int(num) for num in line.strip().split()]

        for i in range(1, len(l)):
            pass

    print(reports)    

    safe = 0

    return safe


def part2(fname):
    return None

if __name__ == "__main__":
    
    print("AOC 2024 DAY 2")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")