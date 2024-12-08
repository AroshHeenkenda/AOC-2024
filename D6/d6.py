
def next_pos(pos, dir):
    i, j = pos
    match dir:
        case "U":
            i -= 1
        case "D":
            i += 1
        case "R":
            j += 1
        case "L":
            j -= 1
        
    return [i, j]

def change_dir(dir):
    match dir:
        case "U":
            return "R"
        case "R":
            return "D"
        case "D":
            return "L"
        case "L":
            return "U"



def is_in(pos, rows, cols):
    i, j = pos

    if i < 0 or i > rows - 1:
        return False
    
    if j < 0 or j > cols - 1:
        return False
    
    return True



def part1(fname):
    
    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    grid = [[char for char in line.strip()] for line in lines]

    pos = [0,0]
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        flag = False
        for j in range(cols):
            if grid[i][j] == "^":
                pos = [i, j]
                flag =True
                break
        if flag:
            break
        
    # Get rid of first bit
    count = 1
    grid[pos[0]][pos[1]] = "X"

    # up, down, left, right
    cur_dir = "U"

    while True:

        # Get next pos
        next = next_pos(pos, cur_dir)

        # Check if in bounds
        if not is_in(next, rows, cols):
            break
            
        # Check if obj
        if grid[next[0]][next[1]] == "#":
            cur_dir = change_dir(cur_dir)

        # Inc count thing
        else:
            if grid[next[0]][next[1]] != "X":
                grid[next[0]][next[1]] = "X"
                count += 1
            pos = next

    for g in grid:
        print(g)
    return count


def part2(fname):

    f = open(fname, "r")
    grid = f.readlines()
    f.close()

if __name__ == "__main__":
    
    print("AOC 2024 DAY 6")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")