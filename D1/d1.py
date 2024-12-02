
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
    
    f = open(fname, "r")
    l1 = []
    l2 = []
    sum = 0
    max_num = 0

    for line in f.readlines():
        r = line.strip().split()
        l1.append(int(r[0]))
        l2.append(int(r[1]))

        # Track max
        if (max(int(r[0]), int(r[1])) > max_num):
            max_num = max(int(r[0]), int(r[1]))
    
    f.close()

    # Create list to track occ
    occ = [0] * (max_num + 1)

    # Iterate through l2 to get occurences of each num
    for num in l2:
        occ[num] += 1
    
    # Get sim sum for each num using occ list
    for num in l1:
        sum += (num * occ[num])

    return sum

if __name__ == "__main__":
    
    print("AOC 2024 DAY 1")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")