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
  pass
def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()