
def check(lst):
    l = [(lst[i] - lst[i-1]) for i in range(1, len(lst))]
    return ((set(l) <= {1, 2, 3}) or (set(l) <= {-1, -2, -3}))

def part1(fname):
    
    f = open(fname, "r")
    safe = 0

    for line in f.readlines():
        levels = [int(num) for num in line.strip().split()]
        if check(levels):
            safe += 1

    f.close() 
    return safe


def part2(fname):

    f = open(fname, "r")
    safe = 0

    for line in f.readlines():

        levels = [int(num) for num in line.strip().split()]
        # Safe
        if check(levels):
            safe += 1
        # Do another check
        else:
            for i in range(len(levels)):
                f_levels = [lvl for l, lvl in enumerate(levels) if l != i]
                if check(f_levels):
                    safe += 1
                    break

    f.close() 
    return safe


    # for report in reports:

    #     r = dif(report)
    #     # It is safe
    #     if check(r):
    #         safe += 1
    #     else:
    #         for i in range(len(r)):
    #             new_report = [el for e, el in enumerate(report) if e != i]
    #             new_r = dif(new_report)
    #             if check(new_r):
    #                 safe += 1
    #                 break



if __name__ == "__main__":
    
    print("AOC 2024 DAY 2")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")