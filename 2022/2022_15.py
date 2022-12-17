with open("AoC_Inputs\Advent_15_22.txt") as f:
    data = f.read().strip().splitlines()

res = []
for row in data:
    s, b = row.split(': ')
    s = s.lstrip("Sensor at ")
    sx, sy = s.split(', ')
    sx, sy = int(sx[2:]), int(sy[2:])
    b = b.lstrip("closest beacon is at ")
    bx, by = b.split(', ')
    bx, by = int(bx[2:]), int(by[2:])
    res.append((sx, sy, bx, by))

def dist(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)

y = 2000000
xx = set()

for sx, sy, bx, by in res:
    x = dist(sx, sy, bx, by) - abs(sy - y)
    xx.update(range(sx - x, sx + x + 1))
    if by == y:
        xx.discard(bx)

print(len(xx))
S=set()
B =set()
sum_d = 0

for line in data:
    words = line.split()
    sx,sy = words[2],words[3]
    bx,by = words[8],words[9]
    sx = int(sx[2:-1])
    sy = int(sy[2:-1])
    bx = int(bx[2:-1])
    by = int(by[2:])
    d = abs(sx-bx) + abs(sy-by)
    sum_d += d
    S.add((sx,sy,d))
    B.add((bx,by))

def valid(x,y,S):
    for (sx,sy,d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return False
    return True

n_checked = 0
found_p2 = False
for (sx,sy,d) in S:
    for dx in range(d+2):
        dy = (d+1)-dx
        for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            n_checked += 1
            x = sx+(dx*signx)
            y = sy+(dy*signy)
            if not(0<=x<=4000000 and 0<=y<=4000000):
                continue
            assert abs(x-sx)+abs(y-sy)==d+1
            if valid(x,y,S) and (not found_p2):
                print(x*4000000 + y)
                found_p2 = True