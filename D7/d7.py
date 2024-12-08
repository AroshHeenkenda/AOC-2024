from collections import defaultdict

def parseinput(fname):

    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    out = []

    for line in lines:
        target, nums = line.strip().split(": ")
        out.append(tuple([int(target), list(map(int, nums.split()))]))
    
    return out


def calibrate_p1(nums):
    n = len(nums)
    dp = []
    dp.append([nums[0]])

    for i in range(1, n):
        cur = nums[i]
        next_dp = []

        for d in dp[i-1]:
            next_dp.append(d * cur)
            next_dp.append(d + cur)
        
        dp.append(set(next_dp))
    
    return dp


def calibrate_p2(nums):
    n = len(nums)
    dp = []
    dp.append([nums[0]])

    for i in range(1, n):
        cur = nums[i]
        next_dp = []

        for d in dp[i-1]:
            next_dp.append(d * cur)
            next_dp.append(d + cur)
            next_dp.append(int(str(d)+str(cur)))
        
        dp.append(set(next_dp))
    
    return dp


def part1(fname):

    equations = parseinput(fname)
    sum_eq = 0

    for target, nums in equations:
        c = calibrate_p1(nums)
        if target in c[-1]:
            sum_eq += target

    return sum_eq


def part2(fname):

    equations = parseinput(fname)
    sum_eq = 0

    for target, nums in equations:
        c = calibrate_p2(nums)
        if target in c[-1]:
            sum_eq += target

    return sum_eq   

if __name__ == "__main__":
    
    print("AOC 2024 DAY 7")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")