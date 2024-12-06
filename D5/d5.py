
def part1(fname):
    
    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    pairs = []
    page_list = []
    passed = False
    max_page = 0

    # Pre-processing
    for line in lines:
        l = line.strip()

        if l == "":
            passed = True
            continue
        
        # Passed the space
        if passed:
            p = [int(num) for num in l.split(",")]
            page_list.append(p)

        else:
            l1, l2 = l.split("|")
            max_page = max(max_page, int(l1), int(l2))
            pairs.append((int(l1), int(l2)))

    page_dict = [ [False] * (max_page + 1)] * (max_page + 1)

    for pair in pairs:

        p1, p2 = pair
        
        page_dict[p2][p1] = True
    
    page_sum = 0

    for pages in page_list:

        valid = True
        for i in range(len(pages)-1, -1, -1):

            for j in range(len(pages)-2, -1, -1):
                if page_dict[i][j]:
                    valid = False
                    break
            
            if not valid:
                break
        
        if valid:
            page_sum += pages[len(pages)//2]


    return page_sum



def part2(fname):
    pass

if __name__ == "__main__":
    
    print("AOC 2024 DAY 5")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")