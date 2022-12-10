with open("Aoc_Inputs\Advent_09_22.txt") as f:
    content = [x.split(" ") for x in f.read().split("\n")[:~0]]

adds = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}

def rope(length):
    knots = [[0, 0] for _ in range(length)]
    visited = set()
    visited.add((0,0))
    for line in content:
        dir,amount = line
        for _ in range(int(amount)):
            knots[0][0] += adds[dir][0]
            knots[0][1] += adds[dir][1]
            for i in range(1, len(knots)):
                posx = knots[i-1][0] - knots[i][0]
                posy = knots[i-1][1] - knots[i][1]
                if max(abs(posx), abs(posy)) > 1:
                    knots[i][0] += (1 if posx > 0 else 0 if posx == 0  else -1)
                    knots[i][1] += (1 if posy > 0 else 0 if posy == 0 else -1)
            visited.add(tuple(knots[-1]))
    return len(visited)
        
print(rope(2))
print(rope(10))