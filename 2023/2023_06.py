file_name = "AoC_Inputs\Advent_2023\Advent_06_23.txt"

with open(file_name, "r") as f:
  data = [line.strip() for line in f.readlines()]

def Part1():
  times = [int(t) for t in data[0][11:].split(' ') if len(t) > 0]
  dists = [int(d) for d in data[1][11:].split(' ') if len(d) > 0]

  tot = 0
  for index in range(len(times)):
    time = times[index]
    dist = dists[index]
    tot = wins(time, dist, tot)
  print(tot)

def Part2():
  times = [t for t in data[0][11:].split(' ') if len(t) > 0]
  dists = [d for d in data[1][11:].split(' ') if len(d) > 0]
  time = int("".join(times))
  dist = int("".join(dists))

  tot = 0
  tot = wins(time, dist, tot)
  print(tot)

def wins(time, dist, tot):
  wins_tot = 0
  for i in range(1, time-1):
    speed  = i
    time_left = time - i
    if speed * time_left > dist:
      wins_tot += 1
  if tot == 0:
    tot = wins_tot
  else:
    tot *= wins_tot
  return tot

def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()