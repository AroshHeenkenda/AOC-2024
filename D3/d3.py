import re

def calc_mul(str):

    nums = (str[4:])[:-1]
    n1, n2 = nums.split(",")
    return (int(n1) * int(n2))


def part1(fname):
    
    # Regex pattern for mul(x{xx},x{xx})
    pat = re.compile('mul\(\d{1,3},\d{1,3}\)')

    f = open(fname, "r")
    code = ''.join(f.readlines())
    f.close()
    
    matches = pat.findall(code)
    sum = 0

    for m in matches:
        sum += calc_mul(m)

    return sum

def part2(fname):
    pass

if __name__ == "__main__":
    
    print("AOC 2024 DAY 3")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")