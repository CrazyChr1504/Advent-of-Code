with open("AoC_Inputs\Advent_2023\Advent_03_23.txt", "r") as data:
  data = data.read().split()

symbol_set = set()
symbol_location = set()
gear_location = set()
for y, i in enumerate(data):
  for x, j in enumerate(i):
    if j != "." and not(j.isnumeric()):
      symbol_set.add(j)
      symbol_location.add((x, y))
      if j == "*":
        gear_location.add((x, y))

num_list = []
active_num = False
width = len(data[0])
for y, line in enumerate(data):
  for x, i in enumerate(line):
    if not(active_num) and (i == "." or i in symbol_set):
      continue
    elif not(active_num) and i.isnumeric():
      num = i
      active_num = True
      NewX1 = x
    elif active_num and (i == "." or i in symbol_set):
      NewNum = int(num)
      NewX2 = x-1
      num_list.append((NewNum, NewX1, NewX2, y))
      active_num = False
      num = ""
    elif active_num and i.isnumeric():
      num += i
      if x == width - 1:
        NewNum = int(num)
        NewX2 = x
        num_list.append((NewNum, NewX1, NewX2, y))
        active_num = False
        num = ""

def Part1():
  p1 = 0
  for num, X1, X2, Y in num_list:
    border = set()
    for y in range(Y-1,Y+2):
      for x in range(X1-1,X2+2):
        border.add((x, y))
      IntersectSet = symbol_location & border
    if len(IntersectSet) > 0:
      p1 += num
  return p1

def Part2():
  p2 = 0
  for gx, gy in gear_location:
    gear_border = set()
    gear_nb = []
    for x in range(gx-1,gx+2):
      for y in range(gy-1,gy+2):
        gear_border.add((x,y))
    for num, x1, x2, y in num_list:
      if (x1, y) in gear_border or (x2, y) in gear_border:
        gear_nb.append(num)
    if len(gear_nb) == 2:
      gear_part1, gear_part2 = gear_nb
      p2 += gear_part1*gear_part2
  return p2

print(Part1())
print(Part2())