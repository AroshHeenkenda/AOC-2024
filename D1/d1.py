

def part1(fname):
    
    f = open(fname, "r")
    l1 = []
    l2 = []
    sum = 0

    for line in f.readlines():
        r = line.strip().split()
        l1.append(int(r[0]))
        l2.append(int(r[1]))
    
    f.close()

    l1.sort()
    l2.sort()

    for i in range(len(l2)):
        sum += abs(l1[i] - l2[i])
    
    return sum


def part2(fname):
    pass

if __name__ == "__main__":
    
    out1 = part1("input1.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input1.txt")
    print(f"Part 2: {out2}")