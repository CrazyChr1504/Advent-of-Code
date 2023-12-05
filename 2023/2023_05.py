file_name = "AoC_Inputs\Advent_2023\Advent_05_23.txt"
with open(file_name, "r") as f:
  data = f.read().split("\n\n")
seeds = [int(x) for x in data[0].split(":")[1].split()]
mappings = [[[int(i) for i in line.split(" ")] for line in mapping.splitlines()[1:]] for mapping in data[1:]]

def Part1():
  vals = seeds
  for mapping in mappings:
    new_vals = []
    for val in vals: 
      new_val = val
      for dest, start, size in mapping:
        if start <= val < start + size:
          new_val = val - start + dest
          break
      new_vals.append(new_val)
    vals = new_vals
  print(min(vals))

def Part2():
  mapping = []
  for i in range(1, len(data)):
    mapping.append([[int(x) for x in s.split()] for s in data[i].split("\n")[1:]])

  def get_min(ranges):
    for i in range(len(mapping)):
      new_ranges = []
      for j in range(len(mapping[i])):
        start = mapping[i][j][1]
        end = mapping[i][j][1] + mapping[i][j][2] - 1
        cut_ranges = []
        for r in ranges:
          if not (end < r[0] or r[1] < start):
            c1 = max(start, r[0])
            c2 = min(end, r[1])
            new_ranges.append((c1 + mapping[i][j][0] - mapping[i][j][1], c2 + mapping[i][j][0] - mapping[i][j][1]))
            if r[0] < c1:
              cut_ranges.append((r[0],c1-1))
            if r[1] > c2:
              cut_ranges.append((c2+1,r[1]))
          else:
            cut_ranges.append(r)
        ranges = cut_ranges
      ranges = cut_ranges + new_ranges
    return min(r[0] for r in ranges)
  
  seed_nums = []
  for i in range(0, len(seeds), 2):
    seed_nums.append((seeds[i], seeds[i+1] + seeds[i] - 1))
  print(get_min(seed_nums))
  
def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()