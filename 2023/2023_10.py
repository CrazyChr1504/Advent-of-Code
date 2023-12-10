
with open("AoC_Inputs\Advent_2023\Advent_10_23.txt", "r") as f:
    data_list = [lines.strip() for lines in f.read().splitlines()]

maze = {}
for i, line in enumerate(data_list):
  for j, char in enumerate(line):
    maze[i, j] = char
    if char == "S":
      start = (i, j)
      
def Part1():
  answer1 = []
  for cur_sign in ["-", "|", "J", "7", "F", "L"]:
    for cur_dir in ["L", "R", "U", "D"]:
        cur_pos = start
        visited = set()
        while cur_pos not in visited:
          visited.add(cur_pos)
          match cur_dir:
            case "R":
              cur_pos = (cur_pos[0], cur_pos[1] + 1)
              cur_sign = maze[cur_pos]
              match cur_sign:
                case "J": cur_dir = "U"
                case "7": cur_dir = "D"
                case "-": continue
                case _: break
            case "L":
              cur_pos = (cur_pos[0], cur_pos[1] - 1)
              cur_sign = maze[cur_pos]
              match cur_sign:
                case "L": cur_dir = "U"
                case "F": cur_dir = "D"
                case "-": continue
                case _: break
            case "U":
              cur_pos = (cur_pos[0] - 1, cur_pos[1])
              cur_sign = maze[cur_pos]
              match cur_sign:
                case "7": cur_dir = "L"
                case "F": cur_dir = "R"
                case "|": continue
                case _: break
            case "D":
              cur_pos = (cur_pos[0] + 1, cur_pos[1])
              cur_sign = maze[cur_pos]
              match cur_sign:
                case "J": cur_dir = "L"
                case "L": cur_dir = "R"
                case "|": continue
                case _: break
        answer1.append(len(visited))
  print(max(answer1) // 2)

def Part2():
  pass

def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()