
def parseinput(fname):

    f = open(fname, "r")
    line = f.readline().strip()
    f.close()

    id = 0
    ind = 0
    out = []

    while ind != len(line) - 1:

        file = [id] * int(line[ind])
        free = ["."] * int(line[ind + 1])
        out += file + free

        ind += 2
        id += 1
    
    out += [id] * int(line[len(line)-1])
    return out


def part1(fname):
    
    space = parseinput(fname)

    # 2 pointer approach
    l, r = 0, len(space) - 1
    while l < r:

        # Move left to find space
        if space[l] != ".":
            l += 1
        
        # Move right to find file
        if space[r] == ".":
            r -= 1
        
        # Swap if both in right pos
        if (space[l] == ".") and (space[r] != "."):
            space[l], space[r] = space[r], space[l]
            l += 1
            r -= 1

    checksum = 0
    for i in range(len(space)):
        val = space[i]
        if val == ".":
            break
        checksum += i * int(val)

    return checksum


def part2(fname):
    pass

if __name__ == "__main__":
    
    print("AOC 2024 DAY 9")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")