from math import lcm

with open("AoC_Inputs\Advent_2023\Advent_08_23.txt") as f:
    data = [line.strip() for line in f.readlines()]

def steps(pos):
  sum = 0

  while True:
    if pos.endswith("Z"):
      break
    i = instruc[sum % len(instruc)]
    p = words[pos]
    p = p.replace("(", "").replace(")", "").split(", ")
    if i == "L":
      pos = p[0].strip()
    else:
      pos = p[1].strip()
    sum += 1

  return sum

instruc = data[0]
words = {}
for line in data[2:]:
  (a, b) = line.split(" = ")
  words[a] = b

def Part1():
  print(steps("AAA"))

def Part2():
  poses = [w for w in words if w.endswith("A")]
  stepsfor = [steps(pos) for pos in poses]
  print(lcm(*stepsfor))

def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()