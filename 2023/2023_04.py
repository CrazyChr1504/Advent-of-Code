with open("AoC_Inputs\Advent_2023\Advent_04_23.txt") as f:
  data = [line.strip() for line in f.readlines()]
  cards = [1] * len(data)

def Part1():
  total = 0
  for line in data:
    result = scratcher(line)
    if len(result) == 0:
      continue
    total += 2 ** (len(result)-1)
  print(total)


def Part2():
  for index in range(len(data)):
    line = data[index]
    result = scratcher(line)
    if len(result) == 0:
      continue
    for i in range(len(result)):
      cards[index + i + 1] += cards[index]
  print(sum(cards))

def scratcher(line):
  line = line.split(":")[1]
  parts = line.split("|")
  win = parts[0].lstrip().rstrip()
  have = parts[1].lstrip().rstrip()
  winSet = set([w for w in win.split(" ") if len(w) > 0])
  haveSet = set([h for h in have.split(" ") if len(h) > 0])
  result = winSet.intersection(haveSet)
  return result


def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()