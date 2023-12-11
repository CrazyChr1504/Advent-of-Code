file_name = "AoC_Inputs\Advent_2023\Advent_11_23.txt"
with open(file_name, "r") as f:
  data = [lines.strip() for lines in f.read().splitlines()]

sy, sx = len(data), len(data[0])
stars = {(x,y) for y, line in enumerate(data) for x, char in enumerate(line) if char == "#"}
ex = {x for x in range(sy) if not any((x,y) in stars for y in range(sy))}
ey = {y for y in range(sx) if not any((x,y) in stars for x in range(sx))}

def dist_calc(stars, ex, ey, ef):
  return sum(dist(a,b,ex,ey,ef) for a in stars for b in stars) // 2

def dist(p1,p2,ex,ey,ef):
  column_row = lambda a,b: range(a,b) if a<b else range(b,a)
  return(
    abs(p1[0]-p2[0])
  + abs(p1[1]-p2[1]) 
  + sum([ef for y in column_row(p1[1],p2[1]) if y in ey])
  + sum([ef for x in column_row(p1[0],p2[0]) if x in ex]) 
  )

def Part1():
  print(dist_calc(stars, ex, ey, 1))

def Part2():
  print(dist_calc(stars, ex, ey, 999_999))

def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()