def import_file():
    with open("Aoc_Inputs\Advent_08_22.txt") as f: 
        return [list(map(int,line)) for line in f.read().splitlines()]
        
def part_one():
    grid  = import_file()
    vis = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            if all(grid[r][x] < k for x in range(c)) or all(grid[r][x] < k for x in range(c+1, len(grid[r]))) or all(grid[x][c] < k for x in range(r)) or all(grid[x][c] < k for x in range(r+1, len(grid))): vis += 1
    print(vis)

def part_two():
    grid  = import_file()
    vis = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            left = right = top = bottom = 0
            for x in range(c - 1, -1, -1):
                left += 1
                if grid[r][x] >= k: break
            for x in range(c + 1, len(grid[r])):
                right += 1
                if grid[r][x] >= k: break
            for x in range(r - 1, -1, -1):
                top += 1
                if grid[x][c] >= k: break
            for x in range(r + 1, len(grid)):
                bottom += 1
                if grid[x][c] >= k: break
            vis = max(vis, left * right * top * bottom)
    print(vis)
            
if __name__ == "__main__":
    part_one()
    part_two()