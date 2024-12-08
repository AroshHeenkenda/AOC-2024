
from collections import defaultdict, deque

def parseinput(fname):

    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    rules = []
    updates = []
    passed = False

    # Pre-processing
    for line in lines:
        l = line.strip()

        # Check for space
        if l == "":
            passed = True
            continue
        
        # Passed the space
        if passed:
            # Page numbers
            update = list(map(int, l.split(',')))
            updates.append(update)

        else:
            # X, Y thing
            rule = tuple(map(int, l.split('|')))
            rules.append(rule)

    return rules, updates


def validate_update(rules, update):
    
    # Extract relevant rules for the update
    update_set = set(update)
    relevant_rules = [(x, y) for x, y in rules if x in update_set and y in update_set]
    
    # Build a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in relevant_rules:
        graph[x].append(y)
        in_degree[y] += 1
    
    # Topological sorting using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if the topological sort matches the update order
    return sorted_order == update


def part1(fname):
    

    rules, updates = parseinput(fname)

    page_sum = 0

    for update in updates:
        if validate_update(rules, update):
            page_sum += update[len(update)//2]

    return page_sum



def part2(fname):
    pass

if __name__ == "__main__":
    
    print("AOC 2024 DAY 5")
    out1 = part1("input.txt")
    print(f"Part 1: {out1}")

    out2 = part2("input.txt")
    print(f"Part 2: {out2}")